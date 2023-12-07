CREATE DATABASE finance_tracker;

USE finance_tracker;

CREATE TABLE
    `users` (
        `user_id` int unsigned NOT NULL AUTO_INCREMENT,
        `user_username` varchar(200) NOT NULL DEFAULT '',
        `user_password` varchar(200) NOT NULL DEFAULT '',
        PRIMARY KEY (`user_id`)
    ) ENGINE = InnoDB;

CREATE TABLE
    `categories` (
        `cat_id` int unsigned NOT NULL AUTO_INCREMENT,
        `cat_name` varchar(200) NOT NULL DEFAULT '',
        PRIMARY KEY (`cat_id`)
    ) ENGINE = InnoDB;

CREATE TABLE
    `transactions` (
        `trans_id` int unsigned NOT NULL AUTO_INCREMENT,
        `user_id` INT REFERENCES users (user_id) ON DELETE CASCADE,
        `cat_id` INT REFERENCES categories (cat_id) ON DELETE SET NULL,
        `amount` DECIMAL(10, 2) NOT NULL,
        `description` VARCHAR(255),
        `trans_date` DATE NOT NULL,
        `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`trans_id`)
    ) ENGINE = InnoDB;

CREATE TABLE
    `budgets` (
        `id` int unsigned NOT NULL AUTO_INCREMENT,
        `cat_id` INT REFERENCES categories (cat_id) ON DELETE SET NULL,
        `amount` DECIMAL(10, 2) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB;

CREATE VIEW get_users AS
SELECT
    user_id,
    user_username,
    user_password
FROM
    users;

CREATE VIEW category_view AS
SELECT
    cat_id,
    cat_name
FROM
    categories;

CREATE VIEW get_transactions AS
SELECT
    t.trans_id,
    t.user_id,
    u.user_username AS user_username,
    t.cat_id,
    c.cat_name AS cat_name,
    t.amount,
    t.description,
    t.trans_date,
    t.created_at
FROM transactions t
INNER JOIN users u ON t.user_id = u.user_id
LEFT JOIN categories c ON t.cat_id = c.cat_id;

DELIMITER $$
CREATE PROCEDURE create_user(
    IN t_username varchar(200),
    IN t_password varchar(200)
)
BEGIN
    INSERT INTO users(user_username, user_password) VALUES(t_username, t_password);
    SELECT LAST_INSERT_ID() AS id;
END$$

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE create_category(
    IN p_cat_name VARCHAR(200)
)
BEGIN
    INSERT INTO categories (cat_name) VALUES (p_cat_name);
     SELECT LAST_INSERT_ID() AS cat_id;
END$$

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE create_transaction(
    IN p_user_id INT,
    IN p_cat_id INT,
    IN p_amount DECIMAL(10, 2),
    IN p_description VARCHAR(255),
    IN p_trans_date DATE
)
BEGIN
    INSERT INTO transactions(user_id, cat_id, amount, description, trans_date) 
    VALUES (p_user_id, p_cat_id, p_amount, p_description, p_trans_date);
    SELECT LAST_INSERT_ID() AS trans_id;
END$$
DELIMITER ;


