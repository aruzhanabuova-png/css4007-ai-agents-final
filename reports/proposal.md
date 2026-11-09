# Project Proposal — Semester Week 10

## Project Title

AI Smart Personal Planner — Intelligent Task and Time Management Agent

## Problem Description

Many people have difficulties managing their time and daily responsibilities. Students have assignments and exams, employees have work deadlines, and other users have personal and household tasks.

It can be difficult to organize multiple tasks, choose priorities, and find enough free time.

My project aims to develop an AI-powered personal planner that helps users organize tasks, manage deadlines, and create personalized daily and weekly schedules.

The AI agent will analyze tasks, deadlines, priorities, and available time to create realistic plans. It will also help users update their schedules when plans change.

## Target Users

- University and college students.
- Employees and working professionals.
- People who want to organize household tasks.
- Anyone who wants to manage their time more effectively.

## Selected Difficulty

C — Intermediate

The application will use an LLM agent that selects and executes tools to manage tasks, check deadlines, find available time, and create personalized schedules.

## Expected Functionality

1. **AI Chat:** Users can communicate with the planner using natural language.
2. **Task Management:** Users can add, view, update, and complete tasks.
3. **Deadline Management:** The application stores deadlines and identifies urgent tasks.
4. **Free Time Management:** Users can enter their available time and existing commitments.
5. **Priority Analysis:** The system prioritizes tasks based on deadlines, importance, and estimated duration.
6. **Smart Planning:** The AI creates daily and weekly schedules.
7. **Schedule Updates:** Users can request changes to their plans.
8. **Progress Tracking:** The application tracks completed and pending tasks.

## Proposed Functions

### 1. add_task()

- **Purpose:** Add a new task to the system.
- **Input:** Task title, category, deadline, priority, and estimated duration.
- **Output:** Created task ID and confirmation.
- **Dependencies:** Python and SQLite.

### 2. get_deadlines()

- **Purpose:** Retrieve tasks with upcoming deadlines.
- **Input:** User ID and optional date range.
- **Output:** List of tasks and their deadlines.
- **Dependencies:** Python and SQLite.

### 3. check_free_time()

- **Purpose:** Find available time slots in the user's schedule.
- **Input:** User ID, date range, and daily availability.
- **Output:** List of available time slots.
- **Dependencies:** Python, datetime, and SQLite.

### 4. create_plan()

- **Purpose:** Create a personalized schedule based on tasks and free time.
- **Input:** Tasks, deadlines, priorities, estimated durations, and available time slots.
- **Output:** A structured daily or weekly plan.
- **Dependencies:** Python, LLM API, and validated scheduling logic.

### 5. update_task()

- **Purpose:** Change task information or completion status.
- **Input:** Task ID and updated fields.
- **Output:** Updated task information or an error message.
- **Dependencies:** Python and SQLite.

### 6. get_progress()

- **Purpose:** Calculate and display task completion progress.
- **Input:** User ID and optional date range.
- **Output:** Completed tasks, pending tasks, and completion percentage.
- **Dependencies:** Python and SQLite.

### 7. save_plan()

- **Purpose:** Save a generated schedule.
- **Input:** User ID and validated plan.
- **Output:** Saved plan ID and confirmation.
- **Dependencies:** Python and SQLite.

### 8. process_message()

- **Purpose:** Process user messages and coordinate the AI agent.
- **Input:** User message and conversation context.
- **Output:** AI response and optional tool execution results.
- **Dependencies:** OpenAI API, Python, and agent tools.

## Proposed Agent Tools

The following functions will be exposed as LLM-callable tools:

**Tool 1: add_task**

Allows the AI agent to create tasks from natural language requests.

**Tool 2: get_deadlines**

Allows the agent to retrieve real task deadlines instead of inventing information.

**Tool 3: check_free_time**

Allows the agent to find available time before creating a schedule.

**Tool 4: create_plan**

Allows the agent to generate a realistic schedule based on task information and available time.

**Tool 5: update_task**

Allows the agent to update existing tasks when the user requests changes.

**Tool 6: get_progress**

Allows the agent to retrieve completion statistics.

The LLM will select tools based on user requests. The application will validate tool arguments, execute the selected functions, and return tool results to the LLM.

The system will use tool results to generate accurate responses. It will not claim that a task or schedule was saved unless the operation succeeds.

## Model Selection

I plan to use an OpenAI GPT model through the OpenAI API.

The model will understand natural language requests, select appropriate tools, and explain generated schedules.

**Proposed technologies:**

- Python — main programming language.
- OpenAI API — LLM integration and tool calling.
- Streamlit — web application interface.
- SQLite — local database for tasks and schedules.
- Python datetime — date and time processing.
- Pytest — automated testing.
- GitHub — version control.

API keys will be stored in environment variables and excluded from GitHub.

## Architecture

The application will use the following architecture:

```text
                 USER
                   |
                   v
          Streamlit Web App
                   |
                   v
             AI Chat Agent
                   |
                   v
           OpenAI GPT Model
                   |
                   v
           Tool Selection
                   |
       +-----------+-----------+
       |           |           |
       v           v           v
   Task Tools   Time Tools   Plan Tools
       |           |           |
       +-----------+-----------+
                   |
                   v
             Python Logic
                   |
                   v
             SQLite Database
                   |
                   v
             Tool Results
                   |
                   v
              AI Response
                   |
                   v
                 USER
```

**Workflow:**

1. The user sends a request through the web interface.
2. The LLM analyzes the request.
3. The LLM selects one or more appropriate tools.
4. Python validates the tool arguments.
5. The selected tools retrieve or update application data.
6. The results are returned to the LLM.
7. The LLM generates a response or a study/work/personal schedule.
8. The user reviews the result.

The application will prevent overlapping tasks and reject invalid time intervals.

## Example Requests

### Example 1 — Study Planning

**User:** "I have three assignments this week and only two free hours tonight. Make a study plan."

**Expected behavior:** The agent checks deadlines and available time, prioritizes assignments, and creates a two-hour study schedule.

### Example 2 — Work Planning

**User:** "I need to finish a report and prepare a presentation before Friday. Organize my work."

**Expected behavior:** The agent adds tasks, checks deadlines, and creates a work schedule.

### Example 3 — Personal Tasks

**User:** "Tomorrow I need to clean my room, buy groceries, and go to the gym."

**Expected behavior:** The agent organizes personal tasks into a daily plan based on available time.

### Example 4 — Schedule Changes

**User:** "I am busy from 3 PM to 5 PM tomorrow. Update my plan."

**Expected behavior:** The agent checks the existing schedule and suggests new time slots without conflicts.

### Example 5 — Progress Tracking

**User:** "How many tasks did I complete this week?"

**Expected behavior:** The agent retrieves task data and displays a progress summary.

## Evaluation Plan

I will evaluate the application using automated tests and manual examples.

**Planned tests:**

1. Add a valid task.
2. Reject a task with invalid information.
3. Retrieve upcoming deadlines correctly.
4. Find available time slots.
5. Detect overlapping time intervals.
6. Generate a schedule within available time.
7. Update an existing task.
8. Calculate task completion progress.
9. Verify that the LLM selects the correct tools.
10. Handle missing information and API errors.

I plan to implement at least 8 automated tests to meet the C-Level requirements.

I will also evaluate whether the generated plans respect deadlines, task priorities, and available time.

Tool execution logs will be saved without exposing private credentials.

## Weekly Milestones

### Week 10 — November 2–8, 2026
**Proposal and Planning**

- Select the project topic and difficulty level.
- Define the problem and target users.
- Describe application functionality.
- Plan functions and agent tools.
- Design the architecture.
- Prepare the evaluation plan.
- Complete the project proposal.

### Week 11 — November 9–15, 2026
**Initial LLM Integration**

- Set up the Python environment.
- Install the required libraries.
- Connect the OpenAI API.
- Create a simple AI chat.
- Test the first LLM request.
- Document the setup process.

### Week 12 — November 16–22, 2026
**Core Functionality**

- Create the SQLite database.
- Implement task creation and retrieval.
- Implement deadline management.
- Add availability management.
- Add input validation and initial tests.

### Week 13 — November 23–29, 2026
**Tool Integration**

- Define LLM-callable tools.
- Connect tools to the LLM.
- Implement real tool execution.
- Validate tool arguments.
- Test tool selection and responses.

### Week 14 — November 30–December 6, 2026
**Agent Workflow**

- Connect task, deadline, and availability tools.
- Implement personalized schedule generation.
- Add task priority analysis.
- Implement schedule updates.
- Demonstrate the complete workflow.

### Week 15 — December 7–13, 2026
**Reliability and Guardrails**

- Handle invalid dates and time intervals.
- Prevent schedule conflicts.
- Handle missing task information.
- Add error handling for API and database failures.
- Improve input and output validation.
- Expand automated tests.

### Week 16 — December 14–20, 2026
**Evaluation and Improvement**

- Run the complete test suite.
- Record test results.
- Analyze scheduling errors.
- Improve agent responses and tool selection.
- Update project documentation.
- Prepare the final report.

### Week 17 — December 21–22, 2026
**Final Submission and Defense**

- Complete the application.
- Finalize the README and reports.
- Run final tests.
- Prepare a working demonstration.
- Submit the GitHub repository link.
- Submit the final commit hash.
- Explain the architecture and tools during the defense.

## AI Assistance Disclosure

I used ChatGPT to help organize the project idea, prepare the proposal, and plan the architecture. I will review, implement, test, and explain the final application myself.