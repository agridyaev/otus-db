import sqlite3

# Path name :memory: for temp DB in RAM
conn = sqlite3.connect('tasks.db')
cur = conn.cursor()

# Create table
cur.execute(
    "CREATE table tasks (id integer primary key autoincrement not null, details text, status text, deadline date)"
)

# Insert one record
cur.execute(
    "INSERT into tasks values (1, 'walk the dog', 'done', '2021-03-23')"
)

# Save (commit) the changes
conn.commit()

# Insert two records using parametrization
query = "INSERT into tasks values (?, ?, ?, ?)"
data = [
    (2, 'prepare breakfast', 'active', '2021-03-24'),
    (3, 'clean the apartment', 'waiting', '2021-03-25')
]
with conn:
    for row in data:
        cur.execute(query, row)

try:
    with conn:
        cur.execute(
            "INSERT into tasks values (1, 'walk the dog', 'done', '2021-03-23')"
        )
except sqlite3.IntegrityError as e:
    print(e)
    print("couldn't walk the dog twice")

# Drop table
cur.execute("DROP table tasks")

conn.close()
