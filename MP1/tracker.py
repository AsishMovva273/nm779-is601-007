from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this; use this task reference for the below requirements
    # update lastActivity with the current datetime value  
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # make sure any checks/conditions clearly display an appropriate message of what failed
    #nm779 10/07/23 This function appears to add a new task to a list called 'tasks' with attributes like name, description, due date, and last activity timestamp. It then attempts to save the updated list and prints a success message or an error message if an exception occurs during the process.
    try:
        task['lastActivity'] = datetime.now()
        task['name'] = name
        task['description'] = description
        task['due'] = str_to_datetime(due)
        tasks.append(task)
        print("new task added successfully")
    except:
        print("error while adding new task, please enter valid info")
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # nm779 10/08/23 This code attempts to update a task's name, description, and due date using user input. It prompts the user for these details based on the task at a specified index in a list of tasks. If the index is invalid (out of range), it informs the user to enter a valid number.
    try:
        task = tasks[index]
        name = input(f"What's the name of this task? {task['name']} \n").strip()
        desc = input(f"What's a brief descriptions of this task? {task['description']} \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) {task['due']} \n").strip()
        update_task(index, name=name, description=desc, due=due)
    except IndexError:
        print("please enter valid number")

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # nm779 10/08/23 This function updates a task in a list called 'tasks' based on input parameters like 'name,' 'description,' and 'due' date. It checks if any of these parameters differ from the task's current values, updates them if necessary, and records the last activity timestamp. Finally, it prints a success message if changes were made and saves the updated task list.
    task = tasks[index]
    task['lastActivity'] = datetime.now()
    x = False
    if name!=task['name']:
        task['name'] = name
        x = True
    if description!=task['description']:
        task['description'] = description
        x = True
    try:
        due = str_to_datetime(due)
        if str(due)!=str(task['due']):
            task['due'] = due
            x = True
    except:
        pass
    if x:
        tasks[index] = task
        print("task updated successfully")
    else:
        print("no new changes")
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
    # if it is currently done, print a message saying it's already been completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # nm779 10/08/23 This function marks a task as completed by updating its 'done' field with the current datetime if the task exists and is not already marked as done. It catches an IndexError if the task index is out of bounds and then saves the updated task list to storage.
    try:
        task = tasks[index]
        if task['done']==False:
            task['done'] = datetime.now()
            tasks[index] = task
        else:
            print("it's already completed")
    except IndexError:
        pass
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution nm779 10/09/23
    task = tasks[index] # <-- replace or update the assignment of this variable, I just used an empty dict so it would run without changes
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # nm779 10/09/23 This function, given a list of tasks, filters and selects tasks that have a due date earlier than the current time. It uses the current time, compares it to each task's due date, and appends eligible tasks to the `_tasks` list. Finally, it calls the `list_tasks` function to display the filtered tasks.
    try:
        del tasks[index]
        print("task deleted successfully")
    except IndexError:
        print("no results")
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # nm779 10/09/23 This function filters a list of tasks, retaining only those with a 'done' key set to False. It then calls the 'list_tasks' function to display the filtered tasks. Essentially, it displays incomplete tasks from the input list of tasks.
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    for task in tasks:
        if task['done']==False:
            _tasks.append(task)
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # nm779 10/09/23 This function creates an empty list called "_tasks" and retrieves the current date and time. It then iterates through a list of tasks, filtering and appending tasks with due dates earlier than the current time to "_tasks." Finally, it calls a "list_tasks" function to display the filtered tasks.
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    now = str_to_datetime(str(datetime.now()).split('.')[0])
    for task in tasks:
        if task['due'] < now:
            _tasks.append(task)
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution 
    # nm779 10/09/23 This function checks the status of a task at a given 'index' in a list of tasks. It calculates the time remaining or overdue for the task's 'due' date compared to the current time and prints the result. If the task is already completed or the index is out of range, it handles the exceptions.
    try:
        task = tasks[index]# <-- this is a placeholder to populate based on the above requirements
        if task['done']==False:
            now = str_to_datetime(str(datetime.now()).split('.')[0])
            if task['due']<now:
                x = []
                x.append(str(now-task['due']).split(','))
                y = x[-1].strip().split(':')
                res = '0 days' if len(x)==1 else x[0]
                print(f"{res}, {y[0]} hours, {y[1]} minutes, {y[2]} seconds overdue")
            else:
                x = []
                x.append(str(task['due']-now).split(','))
                y = x[-1].strip().split(':')
                res = '0 days' if len(x)==1 else x[0]
                print(f"{res}, {y[0]} hours, {y[1]} minutes, {y[2]} seconds remaining")
        else:
            print("task already completed")
    except IndexError:
        pass

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()