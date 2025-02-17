# List to store tasks
tasks = []

def add_task(task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_all_tasks():
    """View all tasks in the list."""
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(task_number):
    """Delete a task from the list."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_all_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
