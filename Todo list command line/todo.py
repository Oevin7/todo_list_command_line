#Todo List Command Line App
print("Welcome to your todo list! Would you like to add, delete, or manage a task?")
user_choice = input()

if user_choice.lower() == "add":
    
    print("Please add your tasks: ")

    with open("todo.txt", "w") as todo_lst:
        user_task = input()

        tasks = []
        tasks.append(user_task)
        
        for task in tasks:
            todo_lst.write(task)
        
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