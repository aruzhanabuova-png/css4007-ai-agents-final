# Semester Week 11 Progress Report

## Completed Work

- Set up Python 3.13 and a virtual environment.
- Installed OpenAI and python-dotenv libraries.
- Configured the OpenAI API key using a .env file.
- Created src/main.py.
- Integrated GPT-4.1-mini using the OpenAI API.
- Implemented the first working LLM request.
- Successfully generated a five-day mathematics exam study plan.
- Created requirements.txt.
- Added basic documentation to README.md.

## Important Commits

- Commit hash: e802718
- Description: Implement Week 11 OpenAI integration and initial prototype.
- Link: https://github.com/aruzhanabuova-png/css4007-ai-agents-final/commit/e802718

## Current Functionality

AI Smart Personal Planner can accept a planning request from the user through the terminal.
The application sends the request to the OpenAI API and displays an AI-generated plan.
For example, the application successfully generated a five-day study plan for a mathematics exam.

## Problems Encountered

PowerShell initially blocked the activation of the Python virtual environment because script execution was restricted.

## Solutions

I temporarily changed the PowerShell execution policy for the current session and successfully activated the virtual environment.
I used a .env file to store the API key securely and configured .gitignore to prevent uploading sensitive information to GitHub.

## What I Learned

I learned how to create and activate a Python virtual environment, install Python libraries, and connect an application to an LLM using the OpenAI API.
I also learned how to manage API keys securely and send user requests to an AI model.

## Next Week

In Week 12, I plan to implement the main planning functions, improve input validation, introduce structured outputs, and add initial tests.
