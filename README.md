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

## Running the API

1) Run the Django system (API)

```
python manage.py runserver
```
2) Open the ```index``` page: 

* Index page: http://127.0.0.1:8000/

3) Open the API

* API-URL: http://127.0.0.1:8000/todo

## Testing the API

The API can be tested using ```curl``` or tools like [Postman](https://www.postman.com/).

### GET and POST using ```curl```

1) [GET] Endpoint to list all TODO tasks: **API-URL/todo**

```
curl http://127.0.0.1:8000/todo
```

2) [POST] Endpoint to create a TODO task: POST **API-URL/todo**

***Note:*** Change the values of "task" and "completed" below before use the ```curl``` command.

```
curl -X POST http://localhost:8000/todo -H "Content-Type: application/json" -d '{"task": "Task Name 1", "completed": "False"}'
```

## Running the API using docker

### Install Docker on Ubuntu

Follow the instructions available on: https://docs.docker.com/engine/install/ubuntu/

### Build the Docker project

```
docker build -t django_project .
```

* Output:

```
[+] Building 20.3s (4/9)                                                                                                                                                                                                       
[+] Building 20.4s (4/9)                                                                                                                                                                                                       
 => [internal] load build definition from Dockerfile                                                                                                                                                                      0.6s
 => => transferring dockerfile: 540B                                                                                                                                                                                      0.0s
[+] Building 20.5s (4/9)                                                                                                                                                                                                       
[+] Building 72.8s (10/10) FINISHED                                                                                                                                                                                            
 => [internal] load .dockerignore                                                                                                                                                                                         0.4s
 => => transferring context: 44B                                                                                                                                                                                          0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                                      0.6s
 => => transferring dockerfile: 540B                                                                                                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:3                                                                                                                                                               1.9s
 => [internal] load build context                                                                                                                                                                                         0.3s
 => => transferring context: 40.26kB                                                                                                                                                                                      0.0s
 => [1/5] FROM docker.io/library/python:3@sha256:...                                                                                                        40.9s
 => => resolve docker.io/library/python:3@sha256:...                                                                                                         0.4s
 ...
 => [2/5] RUN mkdir /code                                                                                                                                                                                                15.7s
 => [3/5] WORKDIR /code                                                                                                                                                                                                   1.6s
 => [4/5] COPY . /code/                                                                                                                                                                                                   1.0s
 => [5/5] RUN pip install -r requirements.txt                                                                                                                                                                             9.2s
 => exporting to image                                                                                                                                                                                                    1.6s
 => => exporting layers                                                                                                                                                                                                   1.5s
 => => writing image sha256:...                                                                                                                              0.1s
 => => naming to docker.io/library/django_project               
```

### See the Docker images

```
docker images
```

* Output

```
REPOSITORY       TAG       IMAGE ID       CREATED              SIZE
django_project   latest    <>   About a minute ago   167MB
```

### To run the Docker container

```
docker run -d -p 8080:8000 django_project
```

where:

* -p 8080:8000: publish the port 8080 to 8000
* django_project: name of the docker container

### To see the status of the the Docker container

```
docker ps
```

### To stop the Docker container

```
docker ps
docker stop <CONTAINER ID>
```

### To remove the Docker image

```
docker images
docker image rm <IMAGE ID> --force
```

### Testing the API running on the Docker container

```
curl -X GET localhost:8080/todo
```

* Output:

``` 
[{"id":1,"task":"Test 1","completed":true},{"id":2,"task":"Learn Python","completed":true},{"id":3,"task":"Learn Django","completed":true},{"id":4,"task":"Learn Rust","completed":false},{"id":5,"task":"Task 2","completed":false},{"id":6,"task":"Task Name 1","completed":false}] 
```

* Readable JSON
```
[
    {
        "id":1,"task":"Test 1",
        "completed":true
    },
    {
        "id":2,"task":"Learn Python",
        "completed":true
    },
    {
        "id":3,"task":"Learn Django",
        "completed":true
    },
    {
        "id":4,"task":"Learn Rust",
        "completed":false
    },
    {
        "id":5,"task":"Task 2",
        "completed":false
    },
    {
        "id":6,"task":"Task Name 1",
        "completed":false
    }
]
```

### Debugging the Docker container

```
docker ps
docker exec -it <CONTAINER id> /bin/bash
```

* Output

```
root@...:/app#

root@...:/app# ls
Dockerfile  README.md  db.sqlite3  manage.py  requirements.txt  todo_api  todo_app

root@...:/app# pwd
/app

root@...:/app# exit
```
