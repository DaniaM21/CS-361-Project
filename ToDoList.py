class ToDoList:
    """
    Represents a to-do list that a user can manage.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes new ToDoList.
        """
        self.name = name
        self._tasks = []

    def getTaskName(self, taskNum: int) -> str:
        """
        Returns the name of the task.
        :param taskNum: number of task
        :return: name of task
        """
        return self._tasks[taskNum - 1]['taskName']

    def getTaskDueDate(self, taskNum: int) -> str:
        """
        Returns the due date of the task.
        :param taskNum: number of task
        :return: due date of task
        """
        return self._tasks[taskNum - 1]['dueDate']

    def getTaskPriority(self, taskNum: int) -> str:
        """
        Returns the priority of the task.
        :param taskNum: number of task
        :return: priority of task
        """
        return self._tasks[taskNum - 1]['priority']
    
    def getTaskNotes(self, taskNum: int) -> str:
        """
        Returns the additional notes of the task.
        :param taskNum: number of task
        :return: additional notes of task
        """
        return self._tasks[taskNum - 1]['taskNotes']

    def addTask(self, taskName: str, dueDate: str, priority: str, taskNotes: str) -> None:
        """
        Adds a task to the to-do list.
        :param taskName: name of task
        :param dueDate: date task is due
        :param priority: priority of task (high/med/low)
        :param taskNotes: any additional task notes
        :return: None
        """
        task = {'taskName': taskName, 'dueDate': dueDate, 'priority': priority, 'taskNotes': taskNotes, 'status': 'Pending'}
        self._tasks.append(task)

    def deleteTask(self, taskNum: int) -> None:
        """
        Deletes a task from the to-do list.
        :param taskNum: number of task to be deleted
        :return: None
        """
        del self._tasks[taskNum - 1]

    def completeTask(self, taskNum: int) -> None:
        """
        Marks a task from the to-do list as complete.
        :param taskNum: number of task to be marked as complete
        :return: None
        """
        self._tasks[taskNum - 1]['status'] = 'Complete'

    def editTask(self, taskNum: int, option: str, newValue: str) -> None:
        """
        Edits a task from the to-do list.
        :param taskNum: number of task to be edited
        :param option: part of task to be edited
        :param newValue: new value of task option
        :return: None
        """
        self._tasks[taskNum - 1][option] = newValue

    def displayTasks(self) -> int:
        """
        Displays all the tasks in the to-do list.
        :return: 0 if there are no tasks in to-do list or 1 otherwise
        """
        if len(self._tasks) == 0:
            print('   no tasks to display')
            return 0
        else:
            for i in range(len(self._tasks)):
                taskName = self._tasks[i]['taskName']
                dueDate = self._tasks[i]['dueDate']
                priority = self._tasks[i]['priority']
                taskNotes = self._tasks[i]['taskNotes']
                if taskNotes == '':
                    taskNotes = 'none'
                status = self._tasks[i]['status']
                print(f'   {i + 1}. {taskName} - Due Date: {dueDate}, Priority: {priority}, Additional Notes: {taskNotes}, Status: {status}')
            return 1
