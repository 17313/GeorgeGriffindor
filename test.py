import sqlite3
def order(statement):
    with sqlite3.connect("BubbleLin.db") as connection:
        c = connection.cursor()
        user_input = statement
        c.execute(user_input)
        results = c.fetchall()
        print(results[0][0])
Additives = int(input('What additives would you like to order?, please type the ID number beside the tea: '))
if Additives in range(1,6):
    order("SELECT Additives FROM Additives WHERE ID == " +str(Additives))
