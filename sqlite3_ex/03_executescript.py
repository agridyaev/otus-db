import sqlite3

# Path name :memory: for temp DB in RAM
conn = sqlite3.connect('tasks.db')

conn.executescript("""
   CREATE table tasks (
       id integer primary key autoincrement not null, 
       details text, 
       status text, 
       deadline date
   );

   INSERT into tasks values (1, 'walk the dog', 'done', '2021-03-23');
   INSERT into tasks values (2, 'prepare breakfast', 'active', '2021-03-24');
   INSERT into tasks values (3, 'clean the apartment', 'waiting', '2021-03-25');
""")

# Drop table
conn.execute("DROP table tasks")

conn.close()
