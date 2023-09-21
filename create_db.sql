-- sql script to automatically create db
-- run using "cat create_db.sql | mysql -hlocalhost -uroot -p"

CREATE DATABASE IF NOT EXISTS pharmakart_db;
CREATE USER IF NOT EXISTS 'pharm_user'@'localhost' IDENTIFIED BY 'Pharmakart!23';
GRANT ALL PRIVILEGES ON pharmakart_db.* TO 'pharm_user'@'localhost';
FLUSH PRIVILEGES;
