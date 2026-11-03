# Employee Management System — Django

A full-featured Employee Management System with 9 pages built with Django.

## Pages Included
1. **Register** — Create a new user account
2. **Login** — Login with username and password
3. **Dashboard** — Employee list with search, view, edit, delete actions
4. **Add Employee** — Form to add a new employee with photo upload
5. **Employee Profile** — View individual employee details
6. **Edit Employee** — Update any employee's information
7. **Delete Employee** — Confirmation page before deleting
8. **Change Password** — Change the logged-in user's password
9. **Logout** — Logout success page

## Setup Instructions

### 1. Prerequisites
- Python 3.9+
- pip

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for Django admin)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Open in browser
```
http://127.0.0.1:8000/
```
You'll be redirected to the login page. Register a new account first, then login.

## Project Structure
```
employee_management/
├── employee_management/       # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── employees/                 # Main app
│   ├── migrations/
│   ├── templates/
│   │   └── employees/
│   │       ├── base.html
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── dashboard.html
│   │       ├── add_employee.html
│   │       ├── employee_profile.html
│   │       ├── edit_employee.html
│   │       ├── delete_employee.html
│   │       ├── change_password.html
│   │       └── logout.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## Features
- User authentication (register, login, logout)
- Full CRUD for employees (create, read, update, delete)
- Profile photo upload
- Employee search/filter
- Password change
- SQLite database (no setup needed)
- Responsive design
