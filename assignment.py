import time
import sys


filepath='product_data.txt'

def search(items):
    search_input = input("What id you like to search for ")
    search_input = int(search_input)

    for item in items:
        if(item.id == search_input):
            print(item.id)
            print(item.name)
            print(item.price)
            print(item.category)
            #return item
        #else:

            #print("Item not found")
            #return None


def update(items):
    updated_input = input("What ID would you like to update? ")        
    updated_input = int(updated_input)

    for item in items:
        if(item.id == updated_input):
            print(item.id)
            print(item.name)
            print(item.price)
            print(item.category)
            updated_data = input("What would you like to update? ")
            if(updated_data == "id"):
                new_id = input("what will the new id be? ")
                item.id = int(new_id)
                print(item.id)
            elif(updated_data == "name"):
                new_name = input("what will the new name be? ")
                item.name = new_name
                print(item.name)
            elif(updated_data == "price"):
                new_price = input("what will the new price be? ")
                item.price = float(new_price) 
                print(item.price)   
            elif(updated_data == "category"):
                new_category = input("what will the new category be? ")
                item.category = (new_category)
                print(item.category) 

def insert(items):
    added_id = input("What id will this new product have? ")               
    added_name = input("What name will this new product have? ")
    added_price = input("What price will this new product have? ")               
    added_category = input("What category will this new product have? ")

    newItem = Item(int(added_id), added_name, float(added_price), added_category)

    items.append(newItem)


def delete(items):    
    removed_id = input("Give the ID for the product you want removed ")
    removed_id = int(removed_id)
    for item in items:
        if(item.id == removed_id):

            items.remove(item)  

def bubbleSort(items): 

    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if items[j].price > items[j+1].price:
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
            #print(f"Step {i*n+j+1}: {items}")
        if not swapped:
            break           

def analyzeSortPerformance(data, description, time_complexity):
    #print(f"\n{description} - Starting array: {data}")
    start = time.time()
    bubbleSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    print(f"Time Complexity: {time_complexity}\n")





with open(filepath, 'r') as file:
   # Read all lines from the file
    lines = file.readlines()

# Define arrays to store specific parts
class Item:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price    
        self.category = category

     


items = []

info = [line.strip().split(', ') for line in lines]

#check if line is not empty
for words in info:

    tempItem = Item(int(words[0]), words[1], float(words[2]), words[3])

    items.append(tempItem)
    

#print(items[0].id)
bubbleSort(items)
for item in items:
        print(item.id)   
        print(item.name)
        print(item.price)
        print(item.category)   

#search(items)
#update(items)
#insert(items)
#search(items)
#delete(items)
#search(items)
   


analyzeSortPerformance(items, "Original Data", "O(n^2)")

data_best = items.copy()

print(data_best)

analyzeSortPerformance(data_best, "Best Case (Sorted)", "O(n)")

data_worst = data_best[::-1]

analyzeSortPerformance(data_worst, "Worst Case (Reverse Sorted)", "O(n^2)")



        
        
        
        












