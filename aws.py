import json

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)

def mark_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}: {status} {task['description']}")

tasks = load_tasks()

while True:
    print("\nChoose an action:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task as complete")
    print("4. View tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        add_task(tasks, description)
    elif choice == "2":
        display_tasks(tasks)
        index = int(input("Enter the index of the task to remove: "))
        remove_task(tasks, index)
    elif choice == "3":
        display_tasks(tasks)
        index = int(input("Enter the index of the task to mark as complete: "))
        mark_complete(tasks, index)
    elif choice == "4":
        display_tasks(tasks)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
