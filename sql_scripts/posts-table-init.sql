-- Create Posts Table
CREATE TABLE posts (
    id INT NOT NULL IDENTITY(1, 1),
    title VARCHAR(150) NOT NULL,
    author VARCHAR(75) NOT NULL,
    body VARCHAR(800) NOT NULL,
    image_path VARCHAR(100),
    timestamp DATETIME DEFAULT GETDATE(),
    user_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert sample post
INSERT INTO posts (title, author, body, user_id) 
VALUES (
    'Sample Post',
    'Admin User',
    'This is a sample post to test the CMS application.',
    1
);
