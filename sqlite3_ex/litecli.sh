# Create table
CREATE table tasks (id integer primary key not null, details text, status text, deadline date);

# Insert records
INSERT into tasks values (1, 'walk the dog', 'done', '2021-03-23');
INSERT into tasks values (2, 'prepare breakfast', 'active', '2021-03-24');
INSERT into tasks values (3, 'clean the apartment', 'waiting', '2021-03-25');

# Get data
SELECT * FROM tasks;
SELECT id, details from tasks;

# Filtering
SELECT * from tasks WHERE status == 'waiting';

# Delete table
DROP table tasks;