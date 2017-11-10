FROM python:latest

LABEL maintainer="robertoachar@gmail.com"

WORKDIR /app

VOLUME [ "/app" ]

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV FLASK_DEBUG=1

EXPOSE 3000

ENTRYPOINT [ "python", "-m", "docker_python_flask" ]
