
Yana_Kapylova
# Django_project ToDo App

# Requirements
- Installed Docker

# How to run the app:
- Open the root app directory
- In terminal run: docker build -t todo .
- Then in terminal run: docker run -d -p 8000:8000 todo
- Run http://127.0.0.1:8000/admin/ in browser
- Use the pre-created superadmin account for tests - **login:** yana **password:** adminyana

# What you can do in the admin site:
- Add new users, change their permissions (manually or using Groups) and status, update their login and password, add info about them, delete them
- Add new Tasks, update then and delete
- Add new Categories, update then and delete

**NOTE:** You won't be able add a task with a non-existent category.

# How to create a new user
- From admin site in the Users tab or go to http://127.0.0.1:8000/todo/register/ and sign up yourself :)

# How to access and use the API endpoints

Tasks:
- **Read all of the existent tasks and create new:** http://127.0.0.1:8000/todo/tasks/
- **Update or delete specific existent task:** /todo/tasks/task_id/, for example, http://127.0.0.1:8000/todo/tasks/6/

Categories:
- **Read all of the existent categories and create new:** http://127.0.0.1:8000/todo/categories/
- **Update or delete specific existent category:** /todo/categories/category_id/, for example, http://127.0.0.1:8000/todo/categories/3/

# UI
I've tried implementing a simple custom UI (based on a project I've made before using localStorage) just for fun :)
You're welcome to visit it https://ykapylova.github.io/todo-ui/

**NOTE:** Keep Django project running at http://127.0.0.1:8000/"
