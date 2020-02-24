# python-alice-skill
## My first implementation of Yandex.Alice skill for Yandex.Dialogs
### It use a Smart Home core

I don't what it will be. Just test smth in Python.

## Build image

To build image with all sources of application use this:
```shell script
docker build --tag alice -f Dockerfile . 
```

## Run container

Use `docker run` to run built application in container with name `alice`:
```shell script
docker run -p 8080:8080 --name alice alice
```

The argument `-p 8080:8080` will expose 8080 port on the host and link it with 8080 container port to access the application.

## Open application

Just open next URL in browser: [http://localhost:8080](http://localhost:8080)