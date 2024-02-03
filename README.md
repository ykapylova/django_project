# django_project
# Yana_Kapylova

# ToDo App

# Requirements
- Installed Docker

# How to run the app:
- Open the root app directory
- In terminal run: docker build -t todo .
- Then in terminal run: docker run -it -p 8000:8000 todo
- Run http://127.0.0.1:8000/admin/ in browser

# What you can do in the admin site:
- Add new users, change their permissions (manually or using Groups) and status, update their login and password, add info about them, delete them
- Add new Tasks, update then and delete
- Add new Categories, update then and delete

**NOTE:** You won't be able add a task with a non-existent category.

# How to access and use the API endpoints
- **Read existent tasks and create new:** http://127.0.0.1:8000/todo/tasks/
- **Update existent tasks:** http://127.0.0.1:8000/todo/tasks/update/task_id/, for example, http://127.0.0.1:8000/todo/tasks/update/4/
- **Delete existent tasks:** http://127.0.0.1:8000/todo/tasks/delete/task_id, for example, http://127.0.0.1:8000/todo/tasks/delete/5/
