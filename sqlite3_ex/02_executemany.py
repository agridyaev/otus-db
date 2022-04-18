import sqlite3

conn = sqlite3.connect('tasks.db')

# Create table
conn.execute(
    "CREATE table tasks (id integer primary key autoincrement not null, details text, status text, deadline date)"
)

# Insert records
query = "INSERT into tasks values (?, ?, ?, ?)"
data = [
    (1, 'walk the dog', 'done', '2021-03-23'),
    (2, 'prepare breakfast', 'active', '2021-03-24'),
    (3, 'clean the apartment', 'waiting', '2021-03-25')
]

with conn:
    conn.executemany(query, data)

# Drop table
conn.execute("DROP table tasks")

conn.close()
