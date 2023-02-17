# Django REST API using docker

## Installation and setup

1) Create python virtual environment

```
python3 -m venv venv
```

2) Activate python virtual environment

```
source venv/bin/activate
```

3) Install python dependencies

* Upgrade pip

```
python3 -m pip install --upgrade pip
```

* Install python dependencies 
```
pip install -r requirements.txt
```

4) Run Django migrations

```
python manage.py migrate
```

5) Create a Django super user to access the database table using the ```/admin``` URL.

```
python manage.py createsuperuser
```

* Create the admin user (username, email and password)

```
Username: admin 
Email address: admin2@gmail.com
Password: <PASSWORD HERE>
Password (again): <PASSWORD HERE>
```

**Note:** To access the ```/admin``` page run the system (```python manage.py runserver```) and open ```http://127.0.0.1:8000/admin```

5) Run the Django system (API)

* Run the Django system

```
python manage.py runserver
```

* Open the ```index``` page: http://127.0.0.1:8000/

6) Open the API

* API-URL: http://127.0.0.1:8000/todo

7) Testing the API

The API can be tested using ```curl``` or tools like [Postman](https://www.postman.com/).

1) [GET] Endpoint to list all TODO tasks: **API-URL/todo**

```
curl http://127.0.0.1:8000/todo
```

2) [POST] Endpoint to create a TODO task: POST **API-URL/todo**

```
curl -X POST http://localhost:8000/todo -H "Content-Type: application/json" -d '{"task": "Task Name 1", "completed": "False"}'
```