import sqlite3

#greeting the customer
print('Welcome to BubbleLin')
print('What would you like to order?')
print("Here is the menu")


#=======================================================================================================================================

#function for showing my menu
def menu(database, category):
    with sqlite3.connect("BubbleLin.db") as connection:    
        c = connection.cursor()
        sql = "SELECT * FROM "+database
        c.execute(sql)
        results = c.fetchall()
        print(category)
        for result in results:
            print("ID: {:0} : {:15} Price: ${:0}" .format(result[0], result[1], result[2]))
        print("\n")
menu("Bubble_tea", "Bubble tea:")
menu("Additives", "Additives:")

#=======================================================================================================================================
        
#showing the bubble tea and additve that the customer ordered
def order(statement):
    with sqlite3.connect("BubbleLin.db") as connection:
        c = connection.cursor()
        user_input = statement
        c.execute(user_input)
        results = c.fetchall()
        return results[0][0]
            
#=======================================================================================================================================

#Asking customer about the vegan and takeaway option
def question(table):   
    while True:
        try:
            if table == "Yes":
                break
            if table == "No":
                break
            if table == "" or  table.isspace() or table.isdigit():
                print('You didnt type "Yes" or "No", else the ordering system will not work')
            else:
                print('You didnt type "Yes" or "No", else the ordering system will not work')
        except:
            print("ADSASDADS")
    return table

#=======================================================================================================================================

while True:    
    #asking the customer for their name
    while True:
        Customer_name = input("What is your name?")
        if Customer_name == "" or  Customer_name.isspace() or Customer_name.isdigit():
            print("Please give a proper name")
            continue
        else:
            break

    #=======================================================================================================================================

    #asking the cutomser what drink theyd like
    while True:
        with sqlite3.connect("BubbleLin.db") as connection:
            while True:    
                try:
                    Bubble_tea = int(input('What bubble tea would you like to order?, please type the ID number beside the tea: '))
                    break
                except:
                    print('Sorry, you didnt type a number. Please type a number in the menu: ')     
            if Bubble_tea in range(1,12):
                a = order("SELECT Bubble_Teas FROM Bubble_tea WHERE ID = " +str(Bubble_tea))
                break
            else:
                print("You didnt type a number inside our known database, please type the ID number beside the tea")

    #=======================================================================================================================================

    #asking what additve they'd like in their drink   
    while True:
        with sqlite3.connect("BubbleLin.db") as connection:
            while True: 
                try:
                    Additives = int(input('What additives would you like to order?, please type the ID number beside the tea: '))
                    break
                except:
                    print('Sorry, you didnt type a number. Please type a number in the menu: ')    
            if Additives in range(1,6):
                b = order("SELECT Additives FROM Additives WHERE ID = " +str(Additives))
                break
            else:
                print("You didnt type a number inside our known database, please type the ID number in the menu")

    print(a, "milk tea with",b)

    #========================================================================================================================================

    #Asking customer about the vegan and takeaway option
    Vegan = input("Would you like dairy in your bubble tea? Please type \"Yes\" or \"No\"")
    x = question(Vegan)
    Takeaway = input("Would you like to Takeaway your drink? Please type \"Yes\" or \"No\"")
    y = question(Takeaway)

    #=======================================================================================================================================

    #inserting the data given into the ordering table
    with sqlite3.connect("BubbleLin.db") as connection:
        c = connection.cursor()
        tuples = (a, b, Customer_name, x, y)
        sql_statement = "INSERT INTO BubbleLin (Bubble_tea, Additives, Customer_name, Vegan, Takeaway) VALUES (?, ?, ?, ?, ?)"
        c.execute(sql_statement,tuples)

    #=======================================================================================================================================
    #print price of bubble tea for customer
    with sqlite3.connect("BubbleLin.db") as connection:
        #telling the customer the total price   
        c = connection.cursor()
        price_1 = "SELECT Price FROM Bubble_tea WHERE ID = " +str(Bubble_tea)
        c.execute(price_1)
        price_of_Bubble_tea = c.fetchall()

    with sqlite3.connect("BubbleLin.db") as connection:
        #telling the customer the total price   
        c = connection.cursor()
        price_2 = "SELECT Price FROM Additives WHERE ID = " +str(Additives)
        c.execute(price_2)
        price_of_Additives = c.fetchall()



total_price = price_of_Bubble_tea + price_of_Additives
print("Thank you" ,Customer_name,"your total is $",total_price[0][0])










