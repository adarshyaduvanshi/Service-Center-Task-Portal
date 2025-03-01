# Service-Center-Task-Portal
Service Center Task Portal

Overview

This is a Service Center Task Portal where users (service center employees) can register, log in, and complete assigned tasks to earn rewards. The system is built using HTML, CSS, Django, and Google authentication.

Features

User Authentication: Register and log in securely (Google authentication included).

Task Management: Tasks assigned by the company.

Progress Tracking: Users can track completed and pending tasks.

Reward System: Users earn rewards based on the number of problems solved.

Dashboard: Users can see pending and completed tasks.

Admin Panel: Company can manage users, tasks, and rewards.

Technologies Used

Frontend: HTML, CSS

Backend: Django (Python)

Database: SQLite (default) or PostgreSQL

Authentication: Google Authentication (OAuth 2.0)

Installation Guide

Clone the repository

git clone https://github.com/your-username/service-center-portal.git
cd service-center-portal
Create a virtual environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
