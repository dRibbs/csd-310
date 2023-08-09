/*
    Title: db_init.sql
    Author: Gillenwater, Sam
    Date: 07AUG2023
    Description: A database initialization script for Whatabook.
*/

-- Drop test user if exists 
DROP USER IF EXISTS 'new_whatabook_user'@'localhost';

-- Create new_whatabook_user and grant them all privileges to the new_whatabook database 
CREATE USER 'new_whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsAwesome!';

-- Grant all privileges to the new_whatabook database to user new_whatabook_user on localhost 
GRANT ALL PRIVILEGES ON new_whatabook.* TO 'new_whatabook_user'@'localhost';

-- Drop constraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY IF EXISTS fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY IF EXISTS fk_user;

-- Drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    Insert store record 
*/
INSERT INTO store(locale)
    VALUES('2000 Old Fort Parkway, Murfreesboro, TN, 37129');

/*
    Insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Moby Dick', 'Herman Melville', 'A tale of a man\'s obsession with a white whale');

INSERT INTO book(book_name, author, details)
    VALUES('Pride and Prejudice', 'Jane Austen', 'A classic novel of manners');

INSERT INTO book(book_name, author, details)
    VALUES('1984', 'George Orwell', 'A dystopian novel about totalitarianism');

INSERT INTO book(book_name, author)
    VALUES('Brave New World', 'Aldous Huxley');

INSERT INTO book(book_name, author)
    VALUES('War and Peace', 'Leo Tolstoy');

INSERT INTO book(book_name, author)
    VALUES('To Kill a Mockingbird', 'Harper Lee');

INSERT INTO book(book_name, author)
    VALUES('The Odyssey', 'Homer');

INSERT INTO book(book_name, author)
    VALUES('The Iliad', 'Homer');

INSERT INTO book(book_name, author)
    VALUES('Don Quixote', 'Miguel de Cervantes');

/*
    Insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Arthur', 'Dent');

INSERT INTO user(first_name, last_name)
    VALUES('Ford', 'Prefect');

INSERT INTO user(first_name, last_name)
    VALUES('Trillian', 'Astra');

/*
    Insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Arthur'), 
        (SELECT book_id FROM book WHERE book_name = 'Moby Dick')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Ford'),
        (SELECT book_id FROM book WHERE book_name = '1984')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Trillian'),
        (SELECT book_id FROM book WHERE book_name = 'Brave New World')
    );
