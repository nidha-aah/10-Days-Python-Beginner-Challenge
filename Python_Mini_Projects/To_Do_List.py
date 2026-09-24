# To-Do List

tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully! ✅")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        task_number = int(input("Enter task number to remove: "))

        if task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(removed_task, "removed successfully! ❌")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice. Try again.")