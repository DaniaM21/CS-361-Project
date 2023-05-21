import time
import requests
from ToDoList import ToDoList

toDoLists = {}

def startMenu():
    """Displays the Start Menu"""
    print('\n')
    print('***** Start Menu *****')
    print('1. Create New To-Do List')
    print('2. Search for a To-Do List')
    print('3. View All To-Do Lists')
    print('4. View All Tasks Organized by Date')
    print('5. Exit')
    print('**********************')

def returnToMenu(listName):
    """Returns user to Edit or Start Menu"""
    return_option = int(input('Enter 1 to return to Edit Menu or 2 to return to Start Menu: '))
    if return_option == 1:
        print('Returning to Edit Menu ...')
        time.sleep(1)
        editMenu(listName)
    elif return_option == 2:
        print('Returning to Start Menu ...')
        time.sleep(1)

def createList():
    """Creates a new To-Do list"""
    print('\n')
    print('***** Create New To-Do List *****')
    
    listName = input('Enter name of To-Do list: ')
    print(f'Your new To-Do list will be called {listName}.')
    
    option = int(input('Enter 1 to Save or 2 to Cancel: '))
    if option == 1:
        toDoLists[listName] = ToDoList(listName)
        print(f'{listName} saved successfully')
    elif option == 2:
        print(f'{listName} was not saved')
    
    print('*********************************')
    
    print('Returning to Start Menu ...')
    time.sleep(1)

def addTask(listName):
    """Adds a task to a To-Do list"""
    print('\n')
    print('***** Add Task *****')
    
    taskName = input('Name of Task: ')
    dueDate = input('Due Date (YYYY-MM-DD): ')
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
        toDoLists[listName].addTask(taskName, dueDate, priority, taskNotes)
        print(f'{taskName} added to {listName} successfully.')
    elif option == 2:
        print(f'{taskName} was not saved')
    
    print('********************')
    
    returnToMenu(listName)

def deleteTask(listName):
    """Deletes a task from a To-Do list"""
    print('\n')
    print('***** Delete Task *****')
    
    print('***')
    print(f'{toDoLists[listName].name}:')
    
    if toDoLists[listName].displayTasks() == 0:
        print('***')
        print('Add tasks to your list before you can delete anything.')
    else:
        print('***')
        
        task = int(input('Enter the number next to the task you want to delete: '))
        
        option = input('Are you sure you want to delete this task? (yes/no): ')
        option = option.lower()
        if option == 'yes':
            toDoLists[listName].deleteTask(task)
            print('Task deleted successfully.')
        elif option == 'no':
            print('Task was not deleted.')
    
    print('***********************')
    
    returnToMenu(listName)

def completeTask(listName):
    """Marks a task as Complete"""
    print('\n')
    print('***** Mark Task as Complete *****')
    
    print('***')
    print(f'{toDoLists[listName].name}:')
    
    if toDoLists[listName].displayTasks() == 0:
        print('***')
        print('Add tasks to your list before you can check anything off.')
    else:
        print('***')
        
        task = int(input('Enter the number next to the task you want to mark as complete: '))
        
        option = input('Are you sure you want to mark this task as complete? (yes/no): ')
        option = option.lower()
        if option == 'yes':
            toDoLists[listName].completeTask(task)
            print('Task marked as complete.')
        elif option == 'no':
            print('Task was not marked as completed.')
    
    print('*********************************')
    
    returnToMenu(listName)

def editTaskIntro(listName):
    """Intro for Edit Task option"""
    print('\n')
    print('***** Edit Task *****')
    
    print('***')
    print(f'{toDoLists[listName].name}:')
    
    if toDoLists[listName].displayTasks() == 0:
        print('***')
        print('Add tasks to your list before you can edit anything.')
        
        returnToMenu(listName)

    else:
        print('***')
        task = int(input('Enter the number next to the task you want to edit: '))
        editTask(listName, task)

def editTask(listName, task):
    """Edits a task's information"""
    
    print('***')
    print(f'1. Name: {toDoLists[listName].getTaskName(task)}')
    print(f'2. Due Date: {toDoLists[listName].getTaskDueDate(task)}')
    print(f'3. Priority: {toDoLists[listName].getTaskPriority(task)}')
    print(f'4. Additional Notes: {toDoLists[listName].getTaskNotes(task)}')
    print('***')
    
    option = int(input('Enter the number next to the item you want to edit: '))
    if option == 1:
        taskName = input('Name of Task: ')
        toDoLists[listName].editTask(task, 'taskName', taskName)
        print(f'Task name changed to {taskName}')
    elif option == 2:
        dueDate = input('Due Date: ')
        toDoLists[listName].editTask(task, 'dueDate', dueDate)
        print(f'Due date changed to {dueDate}')
    elif option == 3:
        priority = input('Priority (Low/Med/High): ')
        toDoLists[listName].editTask(task, 'priority', priority)
        print(f'Priority changed to {priority}')
    elif option == 4:
        taskNotes = input('Additional Notes: ')
        toDoLists[listName].editTask(task, 'taskNotes', taskNotes)
        print(f'Task notes changed to: {taskNotes}')
    
    print('*********************')
    
    return_option = int(input('Enter 1 to edit another part of the task, 2 to return to Edit Menu, or 3 to return to Start Menu: '))
    if return_option == 1:
        editTask(listName, task)
    elif return_option == 2:
        print('Returning to Edit Menu ...')
        time.sleep(1)
        editMenu(listName)
    elif return_option == 3:
        print('Returning to Start Menu ...')
        time.sleep(1)
        
def deleteList(listName):
    """Deletes a To-Do list"""
    print('\n')
    print('***** Delete To-Do List *****')
    
    option = input(f'Are you sure you want to delete {listName}? (yes/no): ')
    option = option.lower()
    if option == 'yes':
        del toDoLists[listName]
        print(f'{listName} deleted successfully.')
        print('*****************************')
        print('Returning to Start Menu ...')
        time.sleep(1)
    elif option == 'no':
        print(f'{listName} was not deleted.')
        print('*****************************')
        
        returnToMenu(listName)

def editMenu(listName):
    """Displays Edit Menu"""
    print('\n')
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
        addTask(listName)
    elif option == 2:
        deleteTask(listName)
    elif option == 3:
        completeTask(listName)
    elif option == 4:
        editTaskIntro(listName)
    elif option == 5:
        deleteList(listName)
    elif option == 6:
        print('Returning to Start Menu ...')
        time.sleep(1)

def searchLists():
    """Searches for a To-Do list by name"""
    print('\n')
    print('***** Search for a To-Do List *****')
    
    listName = input('Enter name of To-Do list: ')
    
    print('Searching ...')
    time.sleep(1)
    
    if listName not in toDoLists:
        print(f'Could not find {listName} in your To-Do lists.')
    else:
        print('***')
        print(f'{toDoLists[listName].name}:')
        toDoLists[listName].displayTasks()
        print('***')
    
    print('***********************************')
    
    returnToMenu(listName)

def viewLists():
    """Displays all To-Do lists"""
    print('\n')
    print('***** View All To-Do Lists *****')
    
    if len(toDoLists) == 0:
        print('no to-do lists to display')
    else:
        for list in toDoLists:
            print('***')
            print(f'{toDoLists[list].name}:')
            toDoLists[list].displayTasks()
            print('***')
    
    print('********************************')
    
    input('Press any key to return to Start Menu: ')
    print('Returning to Start Menu ...')
    time.sleep(1)

def viewTasksByDate():
    """Displays tasks from every To-Do list organized by date (Microservice)"""
    print('\n')
    print('***** View All Tasks Organized by Date *****')
    
    if len(toDoLists) == 0:
        print('no tasks to display')
    else:
        try:
            url = 'http://localhost:3000/organize'
            
            to_do_list_data = []

            for list in toDoLists:
                to_do_list_data += toDoLists[list].getDueDatesAndTasks()

            response = requests.post(url + '?sortDates=true', json=to_do_list_data)
            organized_tasks = response.json()
        
            for date in organized_tasks:
                print('***')
                print(date)
                for list in organized_tasks[date]:
                    print(f'   {list}:')
                    for task in organized_tasks[date][list]:
                        print(f'    - {task}')
                print('***')
                print('\n')
        except:
            print('The microservice must be running before this option can be used.')
    
    print('********************************************')

    input('Press any key to return to Start Menu: ')
    print('Returning to Start Menu ...')
    time.sleep(1)
