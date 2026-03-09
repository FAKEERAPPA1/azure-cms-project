-- Create Users Table
CREATE TABLE users (
    id INT NOT NULL IDENTITY(1, 1),
    username VARCHAR(64) NOT NULL,
    password_hash VARCHAR(128),
    PRIMARY KEY (id)
);

-- Insert default admin user
-- Password is 'pass'
INSERT INTO users (username, password_hash) 
VALUES ('admin', 'pbkdf2:sha256:260000$salt$5FbavP0zY88IZuXXEMkcIdlWz1eejXvgm7Kn9owD7Ck');
