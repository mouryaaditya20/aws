import json

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    return tasks

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return tasks

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}: {status} {task['description']}")

def toggle_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = not tasks[index]["completed"]
    return tasks

def main():
    tasks = load_tasks()
    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Toggle task completion")
        print("4. View tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            tasks = add_task(tasks, description)
        elif choice == "2":
            display_tasks(tasks)
            index = int(input("Enter task index to remove: "))
            tasks = remove_task(tasks, index)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter task index to toggle: "))
            tasks = toggle_task(tasks, index)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
