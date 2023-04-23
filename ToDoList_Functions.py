import time

def startMenu():
    print('***** Start Menu *****')
    print('1. Create New To-Do List')
    print('2. Search for a To-Do List')
    print('3. View All To-Do Lists')
    print('4. Exit')
    print('**********************')

def createList():
    print('***** Create New To-Do List *****')
    listName = input('Enter name of To-Do list: ')
    print(f'Your new To-Do list will be called {listName}.')
    option = int(input('Enter 1 to Save or 2 to Cancel: '))
    if option == 1:
        print(f'{listName} saved successfully')
    elif option == 2:
        print(f'{listName} was not saved')
    print('Returning to Start Menu ...')
    print('*********************************')
    time.sleep(2)

def addTask(listName):
    print('***** Add Task *****')
    taskName = input('Name of Task: ')
    dueDate = input('Due Date: ')
    priority = input('Priority (Low/Med/High): ')
    taskNotes = input('Additional Notes: ')
    print('***')
    print('Task to be added:')
    print(f'   Name: {taskName}')
    print(f'   Due Date: {dueDate}')
    print(f'   Priority: {priority}')
    print(f'   Additional Notes: {taskNotes}')
    print('***')
    option = int(input('Enter 1 to Save task or 2 to Cancel: '))
    if option == 1:
        print(f'{taskName} added to {listName} successfully.')
    elif option == 2:
        print(f'{taskName} was not saved')
    print('********************')
    option = int(input('Enter 1 to return to Edit Menu or 2 to return to Start Menu: '))
    if option == 1:
        print('Returning to Edit Menu ...')
        time.sleep(1)
        editMenu()
    elif option == 2:
        print('Returning to Start Menu ...')
        time.sleep(2)

def deleteTask(listName):
    print('***** Delete Task *****')
    print('***')
    print(f'Contents of {listName} printed')
    print('***')
    print('Enter the number next to the task you want to delete: ')
    option = input('Are you sure you want to delete this task? (yes/no): ')
    option = option.lower()
    if option == 'yes':
        print('Task deleted successfully.')
    if option == 'no':
        print('Task was not deleted.')
    print('***********************')
    option = int(input('Enter 1 to return to Edit Menu or 2 to return to Start Menu: '))
    if option == 1:
        print('Returning to Edit Menu ...')
        time.sleep(1)
        editMenu()
    elif option == 2:
        print('Returning to Start Menu ...')
        time.sleep(2)

def completeTask(listName):
    print('***** Mark Task as Complete *****')
    print('***')
    print(f'Contents of {listName} printed')
    print('***')
    print('Enter the number next to the task you want to mark as complete: ')
    option = input('Are you sure you want to mark this task as complete? (yes/no): ')
    option = option.lower()
    if option == 'yes':
        print('Task marked as complete.')
    if option == 'no':
        print('Task was not marked as completed.')
    print('*********************************')
    option = int(input('Enter 1 to return to Edit Menu or 2 to return to Start Menu: '))
    if option == 1:
        print('Returning to Edit Menu ...')
        time.sleep(1)
        editMenu()
    elif option == 2:
        print('Returning to Start Menu ...')
        time.sleep(2)

def editTaskIntro(listName):
    print('***** Edit Task *****')
    print('***')
    print(f'Contents of {listName} printed')
    print('***')

def editTask(listName):
    print('Enter the number next to the task you want to edit: ')
    print('***')
    print('1. Name: ')
    print('2. Due Date: ')
    print('3. Priority: ')
    print('4. Task Notes: ')
    print('***')
    option = int(input('Enter the number next to the item you want to edit: '))
    if option == 1:
        taskName = input('Name of Task: ')
        print(f'Task name changed to {taskName}')
    elif option == 2:
        dueDate = input('Due Date: ')
        print(f'Due date changed to {dueDate}')
    elif option == 3:
        priority = input('Priority (Low/Med/High): ')
        print(f'Priority changed to {priority}')
    elif option == 4:
        taskNotes = input('Additional Notes: ')
        print(f'Task notes changed to: {taskNotes}')
    print('*********************')
    option = int(input('Enter 1 to edit another part of the task, 2 to return to Edit Menu, or 3 to return to Start Menu: '))
    if option == 1:
        time.sleep(1)
        editTask(listName)
    elif option == 2:
        print('Returning to Edit Menu ...')
        time.sleep(1)
        editMenu(listName)
    elif option == 3:
        print('Returning to Start Menu ...')
        time.sleep(2)
        
def deleteList(listName):
    print('***** Delete To-Do List *****')
    option = input(f'Are you sure you want to delete {listName}? (yes/no): ')
    option = option.lower()
    if option == 'yes':
        print('List deleted successfully.')
    if option == 'no':
        print('List was not deleted.')
    print('*****************************')
    option = int(input('Enter 1 to return to Edit Menu or 2 to return to Start Menu: '))
    if option == 1:
        print('Returning to Edit Menu ...')
        time.sleep(1)
        editMenu()
    elif option == 2:
        print('Returning to Start Menu ...')
        time.sleep(2)

def editMenu(listName):
    print('***** Edit Menu *****')
    print('1. Add Task')
    print('2. Delete Task')
    print('3. Mark Task as Complete')
    print('4. Edit Task')
    print('5. Delete To-Do List')
    print('6. Return to Start Menu')
    print('*********************')
    option = int(input('Enter the number next to the option in the Edit Menu to perform that function: '))
    if option == 1:
        time.sleep(1)
        addTask(listName)
    elif option == 2:
        time.sleep(1)
        deleteTask(listName)
    elif option == 3:
        time.sleep(1)
        completeTask(listName)
    elif option == 4:
        time.sleep(1)
        editTaskIntro(listName)
        editTask(listName)
    elif option == 5:
        time.sleep(1)
        deleteList(listName)
    elif option == 6:
        print('Returning to Start Menu ...')
        time.sleep(2)

def searchLists():
    print('***** Search for a To-Do List *****')
    listName = input('Enter name of To-Do list: ')
    print('Searching ...')
    time.sleep(2)
    print(f'Contents of {listName} printed')
    option = int(input('Enter 1 to enter Edit Menu or 2 to return to Start Menu: '))
    if option == 1:
        print('***********************************')
        time.sleep(1)
        editMenu(listName)
    elif option == 2:
        print('Returning to Start Menu ...')
        print('***********************************')
        time.sleep(2)

def viewLists():
    print('***** View All To-Do Lists *****')
    print('To-Do lists printed')
    print('********************************')
    input('Press any key to return to Start Menu:')
    print('Returning to Start Menu ...')
    time.sleep(2)