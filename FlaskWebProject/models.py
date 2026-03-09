from FlaskWebProject import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from azure.storage.blob import BlobServiceClient
from config import Config
import logging

logger = logging.getLogger(__name__)

# Initialize Blob Service Client
blob_service_client = BlobServiceClient(
    account_url=f"https://{Config.BLOB_ACCOUNT}.blob.core.windows.net",
    credential=Config.BLOB_STORAGE_KEY
)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(75))
    body = db.Column(db.String(800))
    image_path = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def save_changes(self, form, file, user_id, new=False):
        """
        Save post changes to database and upload image to blob storage
        """
        self.title = form.title.data
        self.author = form.author.data
        self.body = form.body.data
        self.user_id = user_id

        # Handle image upload to blob storage
        if file:
            filename = file.filename
            try:
                # Get blob client
                blob_client = blob_service_client.get_blob_client(
                    container=Config.BLOB_CONTAINER,
                    blob=filename
                )
                
                # Upload file to blob storage
                blob_client.upload_blob(file, overwrite=True)
                
                # Store the blob URL in the database
                self.image_path = blob_client.url
                
                logger.info(f'Image uploaded successfully: {filename}')
            except Exception as e:
                logger.error(f'Error uploading image: {str(e)}')
                self.image_path = None

        if new:
            db.session.add(self)
        
        db.session.commit()
