import sys

# List to store tasks
tasks = []

def show_help():
    """Shows the list of available commands."""
    print("""
    Command List:
    - 'add <task>' to add a task
    - 'remove <task_number>' to remove a task
    - 'done <task_number>' to mark a task as done
    - 'list' to show all tasks
    - 'help' to show this help message
    - 'quit' to exit the app
    """)

def add_task(task):
    """Adds a new task."""
    tasks.append({"task": task, "done": False})
    print(f"Added task: {task}")

def remove_task(task_number):
    """Removes a task by its number."""
    try:
        task = tasks.pop(task_number - 1)
        print(f"Removed task: {task['task']}")
    except IndexError:
        print("Invalid task number.")

def mark_task_done(task_number):
    """Marks a task as done."""
    try:
        tasks[task_number - 1]["done"] = True
        print(f"Task {task_number} marked as done.")
    except IndexError:
        print("Invalid task number.")

def list_tasks():
    """Lists all tasks."""
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def main():
    show_help()

    while True:
        command = input("\nEnter command: ").strip().split(" ", 1)
        action = command[0].lower()

        if action == "quit":
            print("Goodbye!")
            sys.exit()

        elif action == "add":
            if len(command) > 1:
                add_task(command[1])
            else:
                print("Please provide a task to add.")

        elif action == "remove":
            if len(command) > 1 and command[1].isdigit():
                remove_task(int(command[1]))
            else:
                print("Please provide a valid task number to remove.")

        elif action == "done":
            if len(command) > 1 and command[1].isdigit():
                mark_task_done(int(command[1]))
            else:
                print("Please provide a valid task number to mark as done.")

        elif action == "list":
            list_tasks()

        elif action == "help":
            show_help()

        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
