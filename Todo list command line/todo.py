#Todo List Command Line App
from datetime import datetime

print("Welcome to your todo list! Would you like to create, add, manage, or delete a task?")
user_choice = input()

if user_choice.lower() == "create":
    
    print("Please create your tasks: ")

    with open("todo.txt", "w+") as todo_lst:
        user_task = input()

        tasks = []
        tasks.append(user_task)
        
        date_added = "Tasks created at " + str(datetime.now())

        todo_lst.writelines(date_added + '\n')
        for task in tasks: 
            todo_lst.writelines("Uncompleted: " + task)

elif user_choice.lower() == "add":
    with open("todo.txt", "a") as todo_lst:
        print("what new tasks would you like to add?")
        user_new = input()
        new_tasks = []
        new_tasks.append(user_new)

        for task in new_tasks:
            todo_lst.write(" " + task)

        
elif user_choice.lower() == "delete":
    
    user_tasks = input("What tasks do you want to delete?\n")
    unwanted_task = []

    unwanted_task.append(user_tasks)
    
    if "," in unwanted_task:
        unwanted_task.remove(",")

    with open("todo.txt") as tasks, open("edited_todo.txt", "w+") as task_file:
        for task in tasks:
            for work in unwanted_task:
                task = task.replace(work, "")
            task_file.write(task)
