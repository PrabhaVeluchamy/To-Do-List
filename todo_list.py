import json
import os

TASK_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""

    if not os.path.exists(TASK_FILE):
        return []

    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""

    try:
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

        print("✅ Tasks saved successfully.")

    except OSError as error:
        print(f"❌ Error saving tasks: {error}")


def add_task(tasks):
    """Add a new task."""

    task_name = input("Enter the task: ").strip()

    if not task_name:
        print("❌ Task cannot be empty.")
        return

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added successfully.")


def display_tasks(tasks):
    """Display all tasks."""

    if not tasks:
        print("\n📋 No tasks available.")
        return

    print("\n" + "=" * 50)
    print("                 TO-DO LIST")
    print("=" * 50)

    for index, task in enumerate(tasks, start=1):

        status = "✓ Completed" if task["completed"] else "○ Pending"

        print(f"{index}. {task['task']} - {status}")

    print("=" * 50)


def complete_task(tasks):
    """Mark a task as completed."""

    if not tasks:
        print("❌ No tasks available.")
        return

    display_tasks(tasks)

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):

            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)

            print("✅ Task marked as completed.")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task(tasks):
    """Delete a task."""

    if not tasks:
        print("❌ No tasks available.")
        return

    display_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            deleted_task = tasks.pop(task_number - 1)

            save_tasks(tasks)

            print(f"🗑️ Deleted task: {deleted_task['task']}")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    """Main application."""

    tasks = load_tasks()

    while True:

        print("\n" + "=" * 50)
        print("             TO-DO LIST APPLICATION")
        print("=" * 50)

        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        print("=" * 50)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)

        elif choice == "6":
            save_tasks(tasks)
            print("\nThank you for using the To-Do List Application!")
            break

        else:
            print("❌ Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()