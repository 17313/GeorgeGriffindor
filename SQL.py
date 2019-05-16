import sqlite3

connection = sqlite3.connect("SQL 1.db")
c = connection.cursor()
sql = "SELECT * FROM Chips"
c.execute(sql)
results = c.fetchall()
for Chips in results:
    print(Chips)