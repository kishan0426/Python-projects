#Assign temporary list
tasks = []



#Set the flag and loop through it
flag = True
while flag == True:
    """Add a selection and perform add, view and exit"""
    selection = input("Type 1 for add ,2 for view, 3 for edit and 4 for exit: ")

    if selection == '1':
        task = input("Enter a todo: ")
        tasks.append(task)
    elif selection == '2':
        for x in tasks:
            print(x.title())
    elif selection == '3':
        new_idx = int(input("Enter the item to be edited and updated on the list, there are {0} items in list : ".format(len(tasks))))
        new_idx -= 1
        tasks[new_idx] = input("Enter the task to be updated: ")
        print("Item is successfully updated")
        for x in tasks:
            print(x)
    elif selection == '4':
        flag = 'False'
    else:
        print("Enter the correct option number given above")
        continue
print()
print('**** Exiting the list ****')