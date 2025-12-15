# 📝 PYTHON CLI To-Do App  Author by HAMZA ARSHAD NAGRA USING GEMINI CLI ON GOOGLE CLOUD-SHELL ENVIRO. 

A clean, fast, and beginner-friendly **Command Line To‑Do application** built with **Python** and **SQLite**. Manage your daily tasks directly from the terminal with a colorful, intuitive interface and persistent storage.

---

## 🌟 Overview

This project is a **robust yet easy-to-understand CLI task manager** designed for productivity and learning. It allows you to **add, view, update, delete, filter, and search tasks** — all from your terminal.

The application is structured like a real-world software project, making it an excellent example of **clean architecture**, **separation of concerns**, and **professional Python coding practices**, while still remaining beginner-friendly.

---

## 🧠 System Design (Simple & Professional)

The app follows a **three-layer architecture**, commonly used in professional software systems:

```
┌───────────────────────────┐
│     Presentation Layer    │
│        (main.py)          │
└─────────────┬─────────────┘
              │
┌─────────────▼─────────────┐
│    Business Logic Layer   │
│        (tasks.py)         │
└─────────────┬─────────────┘
              │
┌─────────────▼─────────────┐
│     Data Access Layer     │
│       (storage.py)        │
└───────────────────────────┘
```

### 📂 Project Structure

```
todo-cli/
│
├── main.py      # CLI menus & user interaction
├── tasks.py     # Task logic & validation
├── storage.py   # SQLite database operations
├── tasks.db     # SQLite database (auto-created)
└── README.md    # Project documentation
```

### 🔹 Layer Responsibilities

- **main.py (Presentation Layer)**
  - Displays menus
  - Handles user input
  - Controls app flow

- **tasks.py (Business Logic Layer)**
  - Defines what a task is
  - Implements add, update, delete, filter, and search logic

- **storage.py (Data Access Layer)**
  - Handles all SQLite operations
  - Keeps database logic isolated from the rest of the app

---
## 🗺️ Application Navigation Map

The application starts at the Main Menu. From there, the user can access various features, including a dedicated sub-menu for listing and searching tasks.

```text
APPLICATION FLOW DIAGRAM
========================

MAIN MENU
│
├── [1] Add Task
│     │
│     ├─ Prompt: Title
│     ├─ Prompt: Description
│     ├─ Prompt: Priority
│     ├─ Prompt: Due Date
│     │
│     └─ Return to Main Menu
│
├── [2] List / Search Tasks
│     │
│     └── List / Search Sub-Menu
│          │
│          ├── [1] Show All Tasks
│          │     ├─ Display all tasks (detailed view)
│          │     └─ Return to List/Search Sub-Menu
│          │
│          ├── [2] Show Pending Tasks
│          │     ├─ Display tasks marked "Not Done"
│          │     └─ Return to List/Search Sub-Menu
│          │
│          ├── [3] Show Completed Tasks
│          │     ├─ Display tasks marked "Done"
│          │     └─ Return to List/Search Sub-Menu
│          │
│          ├── [4] Search Tasks by Keyword
│          │     ├─ Prompt for keyword
│          │     ├─ Search title & description
│          │     └─ Return to List/Search Sub-Menu
│          │
│          └── [0] Back to Main Menu
│                └─ Return to Main Menu
│
├── [3] Mark Task Complete / Incomplete
│     │
│     ├─ Show summarized task list
│     ├─ Prompt for Task ID
│     ├─ Toggle task status (Done / Not Done)
│     │
│     └─ Return to Main Menu
│
├── [4] Update Task
│     │
│     ├─ Show summarized task list
│     ├─ Prompt for Task ID
│     ├─ Update: Title / Description / Priority
│     │
│     └─ Return to Main Menu
│
├── [5] Delete Task
│     │
│     ├─ Show summarized task list
│     ├─ Prompt for Task ID
│     ├─ Confirm and delete task
│     │
│     └─ Return to Main Menu
│
└── [0] Exit
      │
      ├─ Save all changes to database
      └─ Close application safely

```
---

## 💾 Data Storage & Persistence

- Uses **SQLite (`tasks.db`)**, a lightweight, serverless, file-based database
- Database is automatically created on first run
- Tasks are:
  - Loaded on startup
  - Saved instantly on add / update / delete

✅ No data loss
✅ No manual save required

---

## 🎨 User Experience (UX)

This app focuses heavily on **usability**:

- 🌈 **Color-coded terminal output** using `colorama`
- ✅ Clear success and error messages
- 📋 Task summaries shown before update/delete actions
- 🧭 Easy-to-follow menus for non-technical users

---

## ⚙️ Technologies Used

| Technology | Purpose |
|---------|--------|
| Python 3 | Core language |
| SQLite3 | Persistent data storage |
| Colorama | Colored CLI output |

---

## ▶️ How to Run the App

1️⃣ Navigate to the project directory:
```bash
cd /path/to/your/project/todo-cli
```

2️⃣ Run the application:
```bash
python3 main.py
```

The database will be created automatically on first run.

---

## 🚀 Features

### ✅ Core Features

- ➕ **Add Task** (title, description, priority, due date)
- 📄 **List All Tasks** in a clean format
- 🔄 **Toggle Task Status** (Complete / Incomplete)
- ✏️ **Update Task Details**
- ❌ **Delete Tasks Safely**
- 🎯 **Filter Tasks** (Pending / Completed)

### 🌟 Bonus Features

- 🔍 **Keyword Search** (title & description)
- 💽 **SQLite Database Persistence**
- 🎨 **Colorful CLI Interface**
- 🧱 **Professional Multi-File Architecture**

---

## 🤖 How Gemini Code Assist Was Used

Gemini Code Assist acted as an **AI pair programmer** throughout the development process. All generated code was **reviewed, understood, modified, and integrated manually**.

### 🔧 Key Contributions from Gemini

- 🏗 **Project Scaffolding**  
  Helped evolve the project from a single-file script into a clean, modular architecture.

- 🔄 **Data Storage Migration**  
  Assisted in upgrading from JSON-based storage to a robust SQLite database, including schema design and CRUD operations.

- 🐞 **Debugging & Error Resolution**  
  Diagnosed and fixed issues such as module import errors and SQLite operational errors with clear explanations.

- ✨ **Feature Development**  
  Helped implement advanced features like keyword search and task previews before destructive actions.

- 📘 **Documentation & Code Quality**  
  Assisted in improving readability, refactoring logic, and drafting this README.

---

## 🏁 Final Notes

- This project is **hackathon-ready** and follows best practices
- Code is beginner-friendly yet professionally structured
- Easy to extend with features like due-date reminders or analytics
Thank You and have a Great day.


