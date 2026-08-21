# Flask To-Do Web Application

A clean, responsive **full-stack Task Management web application** built with **Python, Flask, Flask-SQLAlchemy, and Jinja2**. The application allows users to manage tasks, track task progress, and maintain persistent task data using SQLite.

## 🚀 Tech Stack 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![HTML5](https://img.shields.io/badge/HTML5-Markup-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-blue?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-yellow?logo=javascript)

## ✨ Key Features

### 📋 Task Management

* Add new tasks.
* View all tasks in an organized list.
* Sequentially update task status:

  * `Pending → Working → Done`
* Clear all tasks.

### 🔐 Authentication Flow

* User login.
* Registration page placeholder.
* Logout functionality.
* Session-based user management.

### 🧩 Modular Architecture

* Uses **Flask Blueprints** for better code organization.
* Separate modules for:

  * Authentication (`auth.py`)
  * Task management (`tasks.py`)

### 🗄️ Database Integration

* SQLite database for persistent storage.
* Flask-SQLAlchemy for database interaction and ORM functionality.
* Database stored inside the Flask `instance` directory.

### 🎨 Modern UI

* Responsive layout.
* Custom gradient headers.
* Task-status badges.
* Clean and simple CSS styling.
* JavaScript support for frontend interactions.

## 📁 Project Directory Structure

```text
Flask App/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   └── tasks.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── scripts.js
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── task.html
│   │
│   ├── __init__.py
│   └── models.py
│
├── instance/
│   └── todo.db
│
└── run.py
```

## 🛠️ Prerequisites

Make sure the following are installed on your system:

* Python 3.x
* pip
* Git
* A code editor such as VS Code

Check Python installation:

```bash
python --version
```

Check pip:

```bash
pip --version
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rohit-js18/flask-todo-app.git
```

### 2. Navigate to the Project Directory

```bash
cd flask-todo-app
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install flask flask-sqlalchemy
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 6. Configure the Application

Make sure the Flask application and database configuration are correctly defined in:

```text
app/__init__.py
app/models.py
```

The SQLite database can be stored as:

```text
instance/todo.db
```

## ▶️ How to Run the Project

From the project root directory, run:

```bash
python run.py
```

The Flask development server should start.

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## 🔄 Application Flow

```text
User
  │
  ▼
Login / Authentication
  │
  ▼
Task Dashboard
  │
  ├── Add Task
  ├── View Tasks
  ├── Update Status
  └── Clear Tasks
  │
  ▼
Flask Routes
  │
  ▼
Flask-SQLAlchemy
  │
  ▼
SQLite Database
```

## 📌 Future Improvements

* Password hashing and secure authentication.
* User-specific task lists.
* Task editing and deletion.
* Task deadlines and priorities.
* Search and filtering.
* REST API integration.
* Deployment using Render, Railway, or another cloud platform.

## 📄 License


```text
MIT License
```

## 👨‍💻 Author

**Your Name**

* GitHub: `https://github.com/rohit-js18`

---

⭐ If you found this project useful, consider giving the repository a star!
