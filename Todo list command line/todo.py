#Todo List Command Line App
from datetime import datetime

print("Welcome to your todo list! Would you like to create or manage a task?")
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

    with open("todo.txt", "r") as task_file:
            modified = task_file.read()

            modified_task_file = modified.replace(",", " ")

    with open("todo.txt", "w") as task_file:
        task_file.write(modified_task_file)


elif user_choice.lower() == "manage":

    print("How would you like to manage your list? Would you like to add or delete, or complete a task?")
    user_manage = input()


    if user_manage.lower() == "add":
        with open("todo.txt", "a") as todo_lst:
            print("what new tasks would you like to add?")
            user_new = input()
            new_tasks = []
            new_tasks.append(user_new)

            for task in new_tasks:
                todo_lst.write(" " + task)

    elif user_manage.lower() == "delete":
    
        user_tasks = input("What tasks do you want to delete?\n")
        unwanted_task = []

        unwanted_task.append(user_tasks)
        
        with open("todo.txt", "r") as task_file:
            deleted_tasks = task_file.read()
            for work in unwanted_task:
                if work in deleted_tasks:
                    modified_task_file = deleted_tasks.replace(work, "")

        with open("todo.txt", "w") as task_file:  
            task_file.write(modified_task_file)
                    


    elif user_manage.lower() == "complete":
        completed_tasks = []
        user_completion = input("Which tasks would you like to mark a completed?\n")
        completed_tasks.append(user_completion)


        with open("todo.txt", "r") as task_file:
            tasks_completed = task_file.read()

        with open("todo.txt", "w") as task_file:
            for task in completed_tasks:
                if task in tasks_completed:
                    modified_task_file = tasks_completed.replace(task, "")
                    task_file.write(modified_task_file)
                else:
                    print("That task is not in the file.")


        with open("todo.txt", "a") as task_file:
            for task in completed_tasks:
                complete_desc = "\nTasks completed at " + str(datetime.now()) + "\nCompleted Tasks: " + task    
            task_file.write(complete_desc)

    else:
        print("That task cannot be performed")
                

else:
    print("That task cannot be performed.")
