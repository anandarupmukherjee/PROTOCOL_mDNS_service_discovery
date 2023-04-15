import sqlite3

# Open a connection to the SQLite database
conn = sqlite3.connect('mdns_services.db')

# Create the services table
conn.execute('''
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    domain TEXT,
    address TEXT,
    port INTEGER,
    timestamp INTEGER
)
''')

# Close the database connection
conn.close()
