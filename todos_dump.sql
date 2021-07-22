PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE todos (
    id INTEGER PRIMARY KEY NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR (12) NOT NULL,
    timestamp DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL
);
INSERT INTO todos VALUES(1,'lalo','In Progress','2021-06-12 18:11:56.915277');
INSERT INTO todos VALUES(2,'Add completion functionality','In Progress','2021-06-12 19:00:44.168699');
INSERT INTO todos VALUES(3,'complete todo app','In Progress','2021-06-16 04:47:20');
COMMIT;