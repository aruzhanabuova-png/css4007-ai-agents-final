# Semester Week 12 Progress Report

## Completed Work

This week, I focused on building the main functions of my AI Smart Personal Planner.

First, I created a SQLite database to store users' tasks. Then, I wrote Python functions to add, view, update, complete, and delete tasks.

I also added some basic input checks and started testing my code with pytest. By the end of the week, I had written 8 tests, and all of them passed.

I also decided to switch from GPT-4.1-mini to GPT-6 Luna. I updated the model in my Python code and tested it with a study planning request. The new model worked successfully and generated a study schedule.

## Important Commits

This week, I worked mainly on these files:

- `src/database.py` — database and task management functions.
- `tests/test_database.py` — tests for the main functions.
- `requirements.txt` — added pytest.

I will commit these changes to GitHub as my Week 12 progress.

## Current Functionality

Right now, my planner can save tasks with their names, categories, deadlines, priorities, and estimated durations.
It can also show saved tasks, mark them as completed, change their priorities, and delete them.
I added checks to prevent users from entering incorrect information, such as an empty task name, an invalid date, or a negative duration.

The AI assistant is not connected to these functions yet. For now, the task management part works separately.

## Problems Encountered

One challenge was making sure that the program would not accept incorrect task information.

Another challenge was testing the database without accidentally changing or deleting real tasks.

## Solutions

To solve the first problem, I added simple validation checks to the Python functions.

For testing, I used pytest with temporary databases. This allowed me to check how the functions work without affecting the main database.

I also checked that the database file is ignored by Git, so it will not be uploaded to GitHub.

## What I Learned

This week, I learned how to create and use a SQLite database in Python.
I also practiced writing SQL queries and learned how to test Python functions using pytest.
The most useful part was seeing how automated tests can help me check whether my code works correctly.

## Next Week

Next week, I want to connect the database functions to my AI assistant.

My main goal is to let the AI use tools to work with tasks, instead of only generating text-based plans.

I plan to add at least two AI tools and test how they handle user requests and incorrect inputs.