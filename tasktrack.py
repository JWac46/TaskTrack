"""A command-line task manager created for CPS 310.

Author: Jackson Waclawski
Course: CPS 310
"""


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Exit")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    task = input("Enter a new task: ")
    #TODO: Use append() to add task to the tasks list.
    tasks.append(task)
    #TODO: Print "Task added successfully."
    print("Task added successfully.")

def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        #TODO: Display the empty-list message.
        print("No tasks to display.")
        return

    print("\nTasks:")

    #TODO: Loop through enumerate(tasks, start=1).
    for i, task in enumerate(tasks, start=1):
        #TODO: Display each number and task using an f-string.
        print(f"{i}. {task}")


def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()