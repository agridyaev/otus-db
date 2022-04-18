import sqlite3

conn = sqlite3.connect('tasks.db')
cur = conn.cursor()

# Create table
cur.execute(
    "CREATE table tasks (id integer primary key not null, details text, status text, deadline date)"
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

query = 'SELECT * FROM tasks'

# treat the cursor as an iterator
for row in cur.execute(query):
    print(row)

# retrieve a single matching row
cur.execute(query)
print(cur.fetchone())

# get a list of two rows
cur.execute(query)
print(cur.fetchmany(size=2))

# get a list of the matching rows
cur.execute(query)
print(cur.fetchall())

conn.close()
