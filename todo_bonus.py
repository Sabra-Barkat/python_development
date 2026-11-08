"""
Project 1 (Bonus): To-Do List with Persistence

Extras beyond the core project:
  * Each task is a dictionary  {"id": 1, "task": "Code", "done": False}
    (a Python dict is like one row of a database table)
  * Mark tasks as done and delete tasks
  * Data is saved to tasks.json, so it survives after the program closes
    (moving data from volatile RAM to permanent storage)
"""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


# ---------- MODEL (data logic) ----------
def load_tasks():
    """Read tasks from disk. Returns an empty list if the file is missing or broken."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    """Serialize the list to JSON and write it to disk."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, text):
    text = text.strip()
    if text == "":
        return False
    new_id = max((t["id"] for t in tasks), default=0) + 1   # next primary key
    tasks.append({"id": new_id, "task": text, "done": False})
    return True


def complete_task(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False


def delete_task(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return True
    return False


# ---------- VIEW (user interface) ----------
def view_tasks(tasks):
    print("\n------ Your To-Do List ------")
    if not tasks:
        print("No tasks yet. Add your first one!")
    else:
        for t in tasks:
            mark = "[x]" if t["done"] else "[ ]"
            print(f"{t['id']:>2}. {mark} {t['task']}")
        done = sum(1 for t in tasks if t["done"])
        print(f"\n{done} of {len(tasks)} tasks completed")
    print("-----------------------------")


def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


def ask_id(prompt):
    value = input(prompt).strip()
    return int(value) if value.isdigit() else None


def main():
    my_tasks = load_tasks()
    print("=" * 30)
    print("   To-Do List - Bonus Edition")
    print("=" * 30)
    print(f"Loaded {len(my_tasks)} saved task(s).")

    try:
        while True:
            show_menu()
            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                if add_task(my_tasks, input("Enter your task: ")):
                    save_tasks(my_tasks)
                    print("Task added and saved.")
                else:
                    print("Task cannot be empty.")
            elif choice == "2":
                view_tasks(my_tasks)
            elif choice == "3":
                if complete_task(my_tasks, ask_id("Task number to mark as done: ")):
                    save_tasks(my_tasks)
                    print("Nice work! Task completed.")
                else:
                    print("No task with that number.")
            elif choice == "4":
                if delete_task(my_tasks, ask_id("Task number to delete: ")):
                    save_tasks(my_tasks)
                    print("Task deleted.")
                else:
                    print("No task with that number.")
            elif choice == "5":
                print("\nGoodbye! Your tasks are saved in tasks.json")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")


if __name__ == "__main__":
    main()
