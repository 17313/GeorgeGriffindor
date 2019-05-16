import random
def generate_array(list_size,min_value,max_value):
        '''returns an array of list size, minimum value and maximum value'''
        myarray = []
        for i in range(list_size):
                myarray.append(random.randint(min_value,max_value))
        return myarray
def linear_search(num, mylist):
        count = 0
        for i in mylist:
                count += 1
                #use an if statement to find value
                if i == num:
                        break
        return count

def selection_sort(Andrew):
        """sort a random list into minmimum to maximum"""
        sorted_list = []

        for i in range(len(Andrew)):
        
                minimum_value = Andrew[0]
                for x in Andrew:
                        if minimum_value > x: 
                                minimum_value = x
                sorted_list.append(minimum_value)
                Andrew.remove(minimum_value)
        
        return sorted_list

def bubble_sort(lists):
        for i in range(len(lists)-1):
                for n in range(len(lists)-1):
                        if lists[n] > lists[n+1]: 
                                lists[n], lists[n+1] = lists[n+1], lists[n]
        return lists

def quick_sort(data):
    """quick sort recrsive algorithm to sort data qickly"""
    if len(data) == 0:
        return data
    #pick a pivot
    pivot = data[0]
    #now check each card left in data with this one and store them in lower or higher or middle
    higher = []
    lower = []
    middle = []
    #now go thorugh each one and copy to correct array
    for value in data:
        if value > pivot:
            higher.append(value)
        elif value < pivot:
            lower.append(value)
        else:
            middle.append(value)
    #now sort the others- returning them in order- recursion is weird.
    return quick_sort(lower) + middle + quick_sort(higher)

binary_search_recurions_count = 0
def binary_search(num,data):
    #global tracker for how many recusrsionssdsdcdm
    global binary_search_recurions_count
    binary_search_recurions_count += 1
    #get element at the half way
    half = len(data) // 2
    if data[half] == num:
        #we found it
        return half
    elif num < data[half]:
        #we can ignore the top half and search again in the bottom half
        return binary_search(num,data[:half])
    elif num > data[half]:
        #we can ignore the bottom half and seacrh again in the top half
        return binary_search(num,data[half+1:]) + (half+1)

        