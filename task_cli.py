import json
import argparse
from datetime import datetime
import os

TASK_FILE = "task.json"

def load_tasks(tasks):
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)
    with open(TASK_FILE, 'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
        
def add_task(description):
    tasks = load_tasks()    
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")
    
def update_task(task_id, new_description):
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = str(datetime.now())
            task_found = True
            break
        if task_found:
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) updated successfully.")
        else:
            print(f"Task with task ID {task_id} not found.")
            
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(tasks) == len(updated_tasks):
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task with ID {task_id} deleted successfully.")
        
def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = tasks if status is None else [task for task in tasks if tasks["status"] == status]
    
    if not filtered_tasks:
        print("No tasks found")
    else:
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
            
def mark_task(task_id, new_status):
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            if new_status in ["in-progress", "done"]:
                task["status"] = new_status
                task["updatedAt"] = str(datetime.now())
                task_found = True
            else:
                print("Invalid status. Use 'in-progress' or 'done'.")
                return
            break
        if task_found:
            save_tasks(tasks)
            print(f"Task (ID: {task_id}) narked as {new_status}.")
        else:
            print(f"Task with ID {task_id} not found.")
                      
    # CLI argument parsing setup
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument('command', help="Command to run (add, update, delete, list, etc)")
    parser.add_argument('args', nargs='*', help="Arguments for the command")
    args = parser.parse_args()
    
    # Command execution
    if args.command == "add":
        add_task(" ".join(args.args))
    elif args.command == "update":
        if len(args.args) < 2:
            print("Please provide a task ID and new description.")
        else:
            update_task(int(args.args[0]), "   ".join(args.args[1:]))
    elif args.command == "delete":
        if len(args.args) < 1:
            print("Please provide a task ID.")
        else:
            delete_task(int(args.args[0]))
    elif args.command == "list":
        if len(args.args) == 0:
            list_tasks()
        else:
            list_tasks(args.args[0]) # 'done', 'todo' or 'in-progress'
    elif args.command == "mark-in-progress":
        if len(args.args) < 1:
            print("Please provide a task ID")
        else:
            mark_task(int(args.args[0]), "in-progress")
    elif args.command == "mark-done":
        if len(args.args) < 1:
            print("Please provide a task ID")
        else:
            mark_task(int(args.args[0]), "done")
    else:
        print("Unknown command.")