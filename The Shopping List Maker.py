#Task 1

def make_shopping_list():
#Empty list for adding items
    shopping_list = []
    print("Start adding items to your shopping list. Type 'done' when finished.")

#Infinite loop so user can keep adding items
    while True:
#User inputs an item
        item = input("Add item: ")
        if item.lower() == 'done':
#Stops the loop when user is done
            break
#Use append to add the item to the list
        shopping_list.append(item)
#The finished list
    return shopping_list
shopping_list = make_shopping_list()
print("Your shopping list includes: ", shopping_list)


#Task 2

def make_shopping_list():
#Empty list for adding items
    shopping_list = []
    print("Start adding items to your shopping list. Type 'done' when finished.")

#Infinite loop so user can keep adding items
    while True:
#User inputs an item
        item = input("Add item: ")
        if item.lower() == 'done':
#Stops the loop when user is done
            break
        elif item.lower() == 'remove':
            remove_item = input("Type the item you want to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} has been removed.")
            else:
                print(f"{remove_item} not found in list")
#Use append to add the item to the list
        else:
            shopping_list.append(item)
#The finished list
    return shopping_list
shopping_list = make_shopping_list()
print("Your shopping list includes: ", shopping_list)


#Task 3

def make_shopping_list():
#Empty list for adding items
    shopping_list = []
    print("Start adding items to your shopping list. Type 'done' when finished.")

#Infinite loop so user can keep adding items
    while True:
#User inputs an item
        item = input("Add item: ")
        if item.lower() == 'done':
#Stops the loop when user is done
            break
        elif item.lower() == 'remove':
            remove_item = input("Type the item you want to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} has been removed.")
            else:
                print(f"{remove_item} not found in list")
#Use append to add the item to the list
        else:
            shopping_list.append(item)
#The finished list
    return shopping_list

def print_shopping_list(shopping_list):
        print("Your shopping list: ")
        for i in range(len(shopping_list)):
#This print statement prints each item with its corresponding index number.
            print(f"{i + 1}. {shopping_list[i]}")

shopping_list = make_shopping_list()
print_shopping_list(shopping_list)