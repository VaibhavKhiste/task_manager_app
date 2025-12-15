Task Manager App

A simple Django + PostgreSQL web application with REST APIs, external API integration, and data visualization.

This project demonstrates CRUD operations, reporting, and API consumption.

Features

CRUD functionality for Tasks via REST APIs

External API integration (weather data and JSONPlaceholder todos)

Task reporting with counts of completed and pending tasks

Data visualization using Chart.js

Admin interface for managing tasks

Tech Stack

Backend: Python, Django, Django REST Framework

Database: PostgreSQL (Supabase)

External API: Open-Meteo (Weather), JSONPlaceholder (Todos)

Frontend Visualization: HTML + Chart.js

Deployment: Any WSGI/ASGI compatible server (e.g., Render, Railway, Heroku)

Installation
Prerequisites

Python 3.10+

PostgreSQL (or Supabase)

Git

Clone Repository
git clone <YOUR_GITHUB_REPO_URL>
cd task_manager_app/backend

Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Mac/Linux

Install Dependencies
pip install -r requirements.txt

Environment Variables

Create a .env file in backend/:

DATABASE_URL=postgresql://username:password@host:port/dbname
SECRET_KEY=your_django_secret_key
DEBUG=True

Database Setup

Run migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser for admin:

python manage.py createsuperuser

Running the Server
python manage.py runserver


API root: http://127.0.0.1:8000/api/

Admin dashboard: http://127.0.0.1:8000/admin/

Task report visualization: http://127.0.0.1:8000/report/

API Endpoints
Endpoint	Method	Description
/api/tasks/	GET, POST	List all tasks / create a new task
/api/tasks/{id}/	GET, PUT, PATCH, DELETE	Retrieve, update, or delete a task
/api/stats/	GET	Task statistics (completed vs pending)
/api/weather/	GET	Fetch current weather data (Pune)
/api/external-todos/	GET	Fetch todos from JSONPlaceholder
/api/report/	GET	Task report (total, completed, pending)
Data Visualization

The /report/ page renders a pie chart showing:

Completed tasks

Pending tasks

Chart updates dynamically from /api/report/ endpoint using Chart.js.

Deployment

Push code to GitHub

Configure environment variables on your cloud platform

Install dependencies and run migrations

Start server (or configure WSGI/ASGI)

Access live application via deployed URL

Optional

Include a 5-minute video explaining your approach

Screenshots of API responses and charts

Author

Vaibhav Khiste
B.Tech in IT | Full Stack & Django Developer