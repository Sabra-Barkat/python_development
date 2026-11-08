"""
Project 1: The To-Do List
DecodeLabs - Python Programming (Lists: append & print loops)

IPO model:
    Input   -> the user types a menu choice / a task
    Process -> add_task() cleans the text and appends it to the list
    Output  -> view_tasks() loops over the list and prints it
"""


def add_task(tasks, task):
    """MODEL: clean the text and store it in the list. Returns True if added."""
    task = task.strip()              # remove accidental spaces
    if task == "":                   # reject empty tasks
        return False
    tasks.append(task)               # the core list operation
    return True


def view_tasks(tasks):
    """VIEW: loop over the list and print every task with its number."""
    print("\n------ Your To-Do List ------")
    if len(tasks) == 0:
        print("No tasks yet. Add your first one!")
    else:
        for number, task in enumerate(tasks, start=1):   # index + value together
            print(f"{number}. {task}")
        print(f"\nTotal tasks: {len(tasks)}")
    print("-----------------------------")


def show_menu():
    """VIEW: print the menu."""
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")


def main():
    my_tasks = []                    # STORAGE: an empty list lives in memory (RAM)

    print("=" * 30)
    print("   Welcome to your To-Do List!")
    print("=" * 30)

    try:
        while True:
            show_menu()
            choice = input("Choose an option (1-3): ").strip()

            if choice == "1":
                new_task = input("Enter your task: ")
                if add_task(my_tasks, new_task):
                    print(f"Added: '{new_task.strip()}'")
                else:
                    print("Task cannot be empty. Please try again.")
            elif choice == "2":
                view_tasks(my_tasks)
            elif choice == "3":
                print("\nGoodbye! Your tasks are cleared from memory when the program ends.")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")


if __name__ == "__main__":       # the gatekeeper: run only when executed directly
    main()
