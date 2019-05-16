'''Andrews program for comparing the time it takes to sort or seach a random array'''
import libraries
import time
import random
'''def sorts(sort):
    start = time.time()
    random_array = libraries.generate_array(list_size,minimum_value,maximum_value)
    a = sort(random_array)
    stop = time.time()
    count = stop - start
    return count

def search(Search):
    start = time.time()
    random_array = libraries.generate_array(list_size,minimum_value,maximum_value)
    quick = sorts(libraries.quick_sort)   
    num_to_find = random.choice(random_array)
    #create variable as tries to print
    tries = Search(num_to_find,quick)
    stop = time.time()
    count = stop - start
    return count,tries

def binary(Binary):
    start = time.time()
    random_array = libraries.generate_array(list_size,minimum_value,maximum_value)
    quick = sorts(libraries.quick_sort)   
    num_to_find = random.choice(quick)
    #create variable as tries to print
    libraries.binary_search(num_to_find,quick)
    stop = time.time()
    count = stop - start
    return count,libraries.binary_search_recurions_count'''


#ask the user
print("hello")
print("we will start by generating an array")
while True:
    try:
        list_size = int(input("what is your range?"))
        minimum_value = int(input("what is your minimum value?"))
        maximum_value = int(input("what is your maximum value?"))
        if minimum_value >= maximum_value:
            print("the minimum value cant be biggger than the maximum, please type a new value")
        else:
            break
        
    except:
        print("please type a number for the questions")


#generate array of users size
random_array = libraries.generate_array(list_size,minimum_value,maximum_value)
print(random_array)
num_to_find = random.choice(random_array)
tries = libraries.linear_search(num_to_find, random_array)

#ask if user would like to sort or search for a value

while True:
    search_sort = input("Please type \"search\" or \"sort\" for the programme to work?")
    if search_sort == "sort":
        #selection = libraries.selection_sort
        start = time.time()
        bubble = libraries.bubble_sort(random_array)
        elapse = time.time() - start
        #quick = libraries.quick_sort()
        #print(selection)
        print("it took", elapse ,"time to sort the list",)
        #print(quick)
        break
    if search_sort == "search":
        linear = libraries.linear_search(num_to_find, random_array)
        #binary = search(libraries.binary_search)
        print("it took", tries ,"tries to find", num_to_find)
        #print(binary)
    '''except:
        print("you didnt print search or sort, the program wont work unless you type one of those words")'''






        
        
        
        
        





#track the time



#sort array using selection sort or bubble sorprint("then we will sort the list")





#work out time

#print time it took to sort array for user






