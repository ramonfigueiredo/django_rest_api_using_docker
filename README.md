Django REST API using docker
===========================

## Contents
1. [System deployment using Docker Compose](#system-deployment-using-docker-compose)
2. [System deployment using only Docker](#system-deployment-using-only-docker)
3. [System deployment on the Linux computer](#system-deployment-on-the-linux-computer)
4. [Testing the API](#testing-the-api)
5. [Docker commands](#docker-commands)
   - [See Docker images](#see-docker-images)
   - [See Docker container status](#see-docker-container-status)
   - [Stop Docker container](#stop-docker-container)
   - [Remove Docker image](#remove-docker-image)
   - [Open Docker container bash](#open-docker-container-bash)



## System deployment using Docker Compose

Just run the following command ```docker compose up``` and the api will be availabe in the endpoint ```http://localhost:8000/todo```

### Build and run

```
docker compose up
```

Or

### Run migrations, build and run
```
docker compose run api python manage.py migrate
docker compose build
docker compose up
```

### Testing the API running on the Docker container

```
curl localhost:8000/todo
```

* Output

```
[{"id":1,"task":"Test 1","completed":true},{"id":2,"task":"Learn Python","completed":true},{"id":3,"task":"Learn Django","completed":true},{"id":4,"task":"Learn Rust","completed":false},{"id":5,"task":"Task 2","completed":false},{"id":6,"task":"Task Name 1","completed":false}]
```

Go back to [Contents](#contents).



## System deployment using only Docker

### Install Docker on Ubuntu

Follow the instructions available on: https://docs.docker.com/engine/install/ubuntu/

### Build the Docker project

#### Using Python 3.7

```
docker build -f Dockerfile_python3 -t django_project .
```

* Output Dockerfile using ```FROM python:3.7-alpine```

```
[+] Building 14.0s (10/10) FINISHED                                                                                                                                                                                            
 => [internal] load .dockerignore                                                                                                                                                                                         0.3s
 => => transferring context: 44B                                                                                                                                                                                          0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                                      0.4s
 => => transferring dockerfile: 548B                                                                                                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:3.7-alpine                                                                                                                                                      0.7s
 => [1/5] FROM docker.io/library/python:3.7-alpine@sha256:...                                                                                                0.0s
 => [internal] load build context                                                                                                                                                                                         0.2s
 => => transferring context: 22.32kB                                                                                                                                                                                      0.0s
 => CACHED [2/5] RUN mkdir /code                                                                                                                                                                                          0.0s
 => CACHED [3/5] WORKDIR /code                                                                                                                                                                                            0.0s
 => [4/5] COPY . /code/                                                                                                                                                                                                   1.4s
 => [5/5] RUN pip install -r requirements.txt                                                                                                                                                                             9.9s
 => exporting to image                                                                                                                                                                                                    1.2s
 => => exporting layers                                                                                                                                                                                                   1.1s
 => => writing image sha256:...                                                                                                                              0.1s 
 => => naming to docker.io/library/django_project         
```

#### Using Python 2.7

**Note:** Skip this section if you already builded the Docker project with python3.7

```
docker build -f Dockerfile_python2 -t django_project .
```

* Output Dockerfile using ```FROM python:2.7-alpine```

```
 => [internal] load .dockerignore                                                                                                                                                                                         0.3s
 => => transferring context: 44B                                                                                                                                                                                          0.0s
 => [internal] load build definition from Dockerfile_python2                                                                                                                                                              0.5s
 => => transferring dockerfile: 549B                                                                                                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:2.7                                                                                                                                                             0.5s
 => [1/5] FROM docker.io/library/python:2.7@sha256:...                                                                                                       0.0s
 => [internal] load build context                                                                                                                                                                                         0.2s
 => => transferring context: 20.88kB                                                                                                                                                                                      0.0s
 => CACHED [2/5] RUN mkdir /code                                                                                                                                                                                          0.0s
 => CACHED [3/5] WORKDIR /code                                                                                                                                                                                            0.0s
 => [4/5] COPY . /code/                                                                                                                                                                                                   1.1s
 => [5/5] RUN pip install -r requirements.txt                                                                                                                                                                             8.9s
 => exporting to image                                                                                                                                                                                                    1.5s
 => => exporting layers                                                                                                                                                                                                   1.4s
 => => writing image sha256:...                                                                                                                              0.0s 
 => => naming to docker.io/library/django_project 
```

### To run the Docker container

```
docker run -d -p 8080:8000 django_project
```

where:

* -p 8080:8000: publish the port 8080 to 8000
* django_project: name of the docker container

### Testing the API running on the Docker container

```
curl -X GET localhost:8080/todo
```

* Output:

``` 
[{"id":1,"task":"Test 1","completed":true},{"id":2,"task":"Learn Python","completed":true},{"id":3,"task":"Learn Django","completed":true},{"id":4,"task":"Learn Rust","completed":false},{"id":5,"task":"Task 2","completed":false},{"id":6,"task":"Task Name 1","completed":false}] 
```

Go back to [Contents](#contents).



## System deployment on the Linux computer

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
Email address: admin@gmail.com
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

Go back to [Contents](#contents).



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

Go back to [Contents](#contents).



## Docker commands

### See Docker images

```
docker images
```

* Output

```
REPOSITORY       TAG       IMAGE ID       CREATED              SIZE
django_project   latest    <>   About a minute ago   167MB
```

### See Docker container status

```
docker ps
```

### Stop Docker container

```
docker ps
docker stop <CONTAINER ID>
```

### Remove Docker image

```
docker images
docker image rm <IMAGE ID> --force
```


### Open Docker container bash

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

Go back to [Contents](#contents).