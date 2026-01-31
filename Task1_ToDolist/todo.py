tasks = []

while True:
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed}' deleted successfully.")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Exiting application.")
        break

    else:
        print("Invalid choice. Please try again.")
