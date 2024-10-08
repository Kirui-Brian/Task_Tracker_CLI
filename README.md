# Task Tracker CLI

## Overview

Task Tracker CLI (<https://roadmap.sh/projects/task-tracker>) is a simple command-line tool designed to help you track and manage your tasks. It allows you to add, update, delete, and list tasks, and mark them as either in-progress or done. All tasks are stored in a local JSON file.

### Features

- Add tasks with descriptions.
- Update or delete existing tasks.
- Mark tasks as `in-progress` or `done`.
- List tasks by their current status (`todo`, `in-progress`, or `done`).
- Tasks are persisted locally in a JSON file.

## Setup

### Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of the terminal/command line.

### Installation

1. **Clone the Repository**

   Open your terminal and clone the repository to your local machine.

   `git clone <https://github.com/Kirui-Brian/task-tracker-cli.git>`
   `cd task-tracker-cli`

2. **Run the Task Tracker CLI**

    You can directly run the Python script from the command line. No external libraries are required since the project only relies on Python’s standard library.

    `python task_cli.py`
    Optional: You can also set an alias to shorten the command for easier use (in Bash/Zsh):

    alias task-cli='`python /path/to/task-tracker-cli/task_cli.py`'
    Usage
    Once you’ve set up the project, you can start managing your tasks by running the CLI commands listed below.

    Add a Task
    To add a new task, use the add command followed by the task description:

    `task-cli add "Buy groceries"`

### Output: Task added successfully (ID: 1)

Update a Task
To update an existing task's description, use the update command followed by the task ID and the new description:

`task-cli update 1 "Buy groceries and cook dinner"`

### Output: Task (ID: 1) updated successfully

Delete a Task
To delete a task by its ID:

`task-cli delete 1`

### Output: Task (ID: 1) deleted successfully

Mark Task as In-Progress or Done
To mark a task as in-progress:

`task-cli mark-in-progress 1`

### Output: Task (ID: 1) marked as in-progress

To mark a task as done:

`task-cli mark-done 1`

### Output: Task (ID: 1) marked as done

List All Tasks
To list all tasks regardless of their status:

`task-cli list`
List Tasks by Status
You can also list tasks by their status (done, todo, or in-progress):

### List tasks that are done

`task-cli list done`

### List tasks that are in-progress

`task-cli list in-progress`

### List tasks that are yet to be done

`task-cli list todo`

#### Task Structure

Each task is stored with the following properties in the JSON file:

`id:` A unique identifier for the task.
`description:` A short description of the task.
`status:` The status of the task (todo, in-progress, done).
`createdAt:` The date and time when the task was created.
`updatedAt:` The date and time when the task was last updated.

#### Example of how tasks are stored in tasks.json:

    ```json
    [
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2024-10-01 10:00:00",
        "updatedAt": "2024-10-01 10:00:00"
    }
    ]
    ```

#### Error Handling

    If you attempt to update, delete, or mark a task that does not exist, the CLI will notify you that the task with the given ID was not found.
    If the JSON file is missing or corrupted, the application will create or reset it when running the first command.

#### Future Improvements

    Add support for setting task priorities.
    Implement task deadlines and reminders.
    Allow for task categories or tags.
    License
    This project is licensed under the MIT License. See the LICENSE file for more details.

    ```arduino

    This `README.md` file provides clear instructions and usage examples for anyone using your Task Tracker CLI. Remember to replace `"https://github.com/Kirui-Brian/task-tracker-cli.git"` with your actual GitHub repository URL.
    ```
