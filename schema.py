instructions=[
    'SET FOREIGN_KEY_CHECKS = 0',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(55) UNIQUE NOT NULL,
            password VARCHAR(65) NOT NULL
        )
    """
    ,
    """
    CREATE TABLE todo (
        id INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        complete BOOLEAN NOT NULL,
        FOREING KEY (created_by) REFERENCES user (id)

        )
    """
]