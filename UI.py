from ToDoList_Functions import *

print('*****')
print('Welcome to To-Doey!')
print('To-Doey lets you manage your to-do lists.')
print('Use the following menu to manage your lists.')
print('*****')

while True:
    startMenu()
    option = int(input('Enter the number next to the option in the Start Menu to perform that function: '))
    if option == 1:
        createList()
    elif option == 2:
        searchLists()
    elif option == 3:
        viewLists()
    elif option == 4:
        viewTasksByDate()
    elif option == 5:
        exit()
    else:
        print('Invalid option. Please try again.')