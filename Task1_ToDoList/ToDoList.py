FILENAME = "tasks.txt"

def view_tasks():
    try:
        file = open(FILENAME, "r")
        tasks = file.readlines()
        file.close()

        if len(tasks) == 0:
            print("No tasks available!")
        else:
            print("\nTo-Do List:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i].strip())

    except FileNotFoundError:
        print("No tasks available!")

def add_task():
    task = input("Enter a task: ")

    file = open(FILENAME, "a")
    file.write(task + "\n")
    file.close()

    print("Task added successfully!")

def delete_task():
    try:
        file = open(FILENAME, "r")
        tasks = file.readlines()
        file.close()

        view_tasks()

        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)

            file = open(FILENAME, "w")
            file.writelines(tasks)
            file.close()

            print("Task deleted successfully!")
        else:
            print("Invalid task number!")

    except FileNotFoundError:
        print("No tasks available!")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
