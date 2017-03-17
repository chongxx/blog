CREATE DATABASE blog;

use blog;

CREATE TABLE user
(
	id 	INT(20) NOT NULL PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	pwd VARCHAR(16) NOT NULL,
	nickname VARCHAR(20) NOT NULL,
	avatar VARCHAR(256),
	state INT(1) NOT NULL,
	register_time INT(16) NOT NULL,
	email VARCHAR(32)
);

CREATE TABLE post
(
	id INT NOT NULL PRIMARY KEY,
	title VARCHAR(225) NOT NULL,
	text TEXT NOT NULL,
	publish_time INT NOT NULL,
	user_id INT NOT NULL
);
