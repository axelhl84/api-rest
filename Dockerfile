
FROM  python:3.8-slim@sha256:f8a12edddd4fb9c9fd38cd7147c5861a596dee5a4852b6bded3d1d6e2c8987bd

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
