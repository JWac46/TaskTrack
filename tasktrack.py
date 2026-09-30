"""A command-line task manager created for CPS 310.

Author: Jackson Waclawski
Course: CPS 310
"""

TASKS_FILE = "task.txt"

def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    task = input("Enter a new task: ").strip()
    
    if not task:
        #TODO: Display the error message.
        print("Error: Task cannot be empty.")
        #TODO: Return without adding a task.
        return
        
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

def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()

                #TODO: Ignore blank lines.
                if not task:
                    continue
                #TODO: Add each non-empty task to the tasks list.
                tasks.append(task)
    except FileNotFoundError:
        # A new project may not have a task file yet.
        return []

    return tasks

def save_tasks(tasks, filename):
    """Save all tasks to a text file."""
    with open(filename, "w") as file:
        #TODO: Loop through the tasks list.
        for task in tasks:
            #TODO: Write each task followed by a newline character.
            file.write(f"{task}\n")


def remove_task(tasks):
    """Prompt the user to select and remove a task.

    Return True when a task is removed and False otherwise.
    """
    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)
    selection = input("Enter the number of the task to remove: ").strip()

    #TODO: Reject input that is not numeric.
    if not selection.isdigit():
        print("Invalid input. Please enter a numeric value.")
        return False

    task_number = int(selection)

    #TODO: Reject numbers outside the valid task range.
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return False

    #TODO: Remove the selected task from the list.
    # Remember that displayed task numbers begin at 1,
    # while Python list indexes begin at 0.
    removed_task = tasks.pop(task_number - 1) 

    #TODO: Display a confirmation containing the removed task.
    print(f"Task removed: {removed_task}")

    return True

def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks, TASKS_FILE)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()