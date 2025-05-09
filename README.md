# TODO App with Django REST Framework and PostgreSQL

A feature-rich TODO application built with Django REST Framework and PostgreSQL.

## Features

- User authentication (login/signup)
- Create, read, update, and delete tasks
- Reorder tasks (drag and drop)
- Add images to tasks
- Add PDF files to tasks (with compression)
- Customize background color and theme for each task
- Set due dates for tasks
- Mark tasks as completed
- Dark mode toggle
- Calendar view for task deadlines
- Highlight tasks with custom colors

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Authentication**: JWT (JSON Web Tokens)
- **File Handling**: Pillow, PyPDF2

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd TODOapp
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure PostgreSQL:
   - Create a database named `todo_db`
   - Update database settings in `todo_drf/todo_project/settings.py` if needed

4. Run migrations:
   ```
   cd todo_drf
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at http://localhost:8000

## API Endpoints

- **Authentication**:
  - `POST /api/token/`: Obtain JWT token
  - `POST /api/token/refresh/`: Refresh JWT token

- **Users**:
  - `POST /api/users/`: Register a new user
  - `GET /api/users/`: Get user profile

- **Tasks**:
  - `GET /api/tasks/`: List all tasks
  - `POST /api/tasks/`: Create a new task
  - `GET /api/tasks/{id}/`: Get a specific task
  - `PUT/PATCH /api/tasks/{id}/`: Update a task
  - `DELETE /api/tasks/{id}/`: Delete a task
  - `POST /api/tasks/{id}/reorder/`: Reorder a task

- **Task Images**:
  - `POST /api/tasks/{id}/images/`: Upload an image for a task
  - `DELETE /api/tasks/{id}/images/{image_id}/`: Delete an image

- **Task Files**:
  - `POST /api/tasks/{id}/files/`: Upload a PDF file for a task
  - `DELETE /api/tasks/{id}/files/{file_id}/`: Delete a file

## Project Structure

```
todo_drf/
├── manage.py
├── media/
│   └── uploads/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   ├── base.html
│   ├── home.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── todo_app/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── views_auth.py
│   └── views_frontend.py
└── todo_project/
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```