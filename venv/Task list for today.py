#Assign temporary list
tasks = []



#Set the flag and loop through it
flag = True
while flag == True:
    """Add a selection and perform add, view and exit"""
    selection = input("Type 1 for add ,2 for view, or 3 for exit: ")

    if selection == '1':
        task = input("Enter a todo: ")
        tasks.append(task)
    elif selection == '2':
        for x in tasks:
            print(x.title())
    elif selection == '3':
        flag = 'False'
    else:
        print("Enter the correct option number given above")
        continue
print()
print('**** Exiting the list ****')