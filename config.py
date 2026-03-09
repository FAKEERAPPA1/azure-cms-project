import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Azure CMS Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    
    # SQL Database Configuration
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    
    # SQL Connection String
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication Configuration
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    
    # Microsoft Authentication Authority
    AUTHORITY = 'https://login.microsoftonline.com/common'
    
    # Redirect path for authentication
    REDIRECT_PATH = '/getAToken'
    
    # Scopes for Microsoft Graph API
    SCOPE = ['User.Read']
    
    # Session configuration
    SESSION_TYPE = 'filesystem'
