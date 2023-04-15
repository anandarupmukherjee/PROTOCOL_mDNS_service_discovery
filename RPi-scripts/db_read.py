import sqlite3

# Open a connection to the SQLite database
conn = sqlite3.connect('mdns_services.db')

# Query the database for the 5 most recent records
cursor = conn.execute("SELECT * FROM services ORDER BY timestamp DESC LIMIT 5")

# Fetch the query results as a list of tuples
results = cursor.fetchall()

# Print the query results
for row in results:
    print(row)

# Close the database connection
conn.close()
