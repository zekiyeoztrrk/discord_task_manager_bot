# discord_task_manager_bot
This bot helps you manage tasks in a Discord server. It offers features such as adding, deleting, showing, and marking tasks as completed. All tasks are stored in an SQLite database.

# Features
Add Task: !add_task <description> — Adds a new task with the given description.
Delete Task: !delete_task <task_id> — Deletes the task with the specified task ID.
Show Tasks: !show_tasks — Displays a list of all current tasks.
Complete Task: !complete_task <task_id> — Marks the task with the given task ID as completed.

# Setup
Prerequisites
- Python 3.x installed on your machine.
- Required libraries specified in requirements.txt.
1. Clone this repository to your local machine.
2. Install the required dependencies using pip.
3. Set up a Discord bot and get your bot token by going to the Discord Developer Portal and creating a new application. Under the "Bot" section, click "Add Bot" and copy the bot token.
4. Add your bot token to the project by either adding it as an environment variable or configuring it in the bot.py file.
5. Start the bot using Python.

# Tests
- To ensure the bot functions correctly, run the provided tests. The tests for adding, deleting, showing, and completing tasks are located in the tests directory.
- If there are any errors during the tests, ensure that the SQLite database is correctly set up and that the task commands are working as expected.

# Project Structure
discord_task_manager_bot:
- bot.py: Main bot logic.
- commands.py: Command handler for bot functions.
- database.py: SQLite database interactions.
- requirements.txt: List of dependencies.
- README.md: Project documentation.
- tests: Unit tests including test_add_task.py, test_delete_task.py, test_show_tasks.py, test_complete_task.py.


