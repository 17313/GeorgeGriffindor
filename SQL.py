import sqlite3
    
with sqlite3.connect("BubbleLin.db") as connection:    
    c = connection.cursor()
    sql = "SELECT * FROM Bubble_tea"
    c.execute(sql)
    results = c.fetchall()
    for result in results:
        print("BubbleLin: {0:15} Price: ${1:0}" .format(result[1], result[2]))
