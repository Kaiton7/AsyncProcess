# Asynchronous Tasks with Django and Celery
This Repository is an extension of the following [post](https://testdriven.io/blog/django-and-celery/).

# Extended Feature by Kaito
- Monitoring the progress of the process.
- Downloading the results of the process.
- function to upload a configuration file from client to change the process handling.
- Visualization using Datatable.js.
- 


Example of how to handle background processes with Django, Celery, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-and-celery/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to http://localhost:1337 to view the app or to http://localhost:5555 to view the Flower dashboard.

Trigger a new task:
- upload a config file( in the ./project/configfile/).
- click the execute button.