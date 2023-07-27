FROM python:3.10

RUN pip install pipenv

WORKDIR /app

COPY . /app

RUN pipenv sync --system

EXPOSE 3000

CMD ["gunicorn", "flaskr:create_app()", "-b 0.0.0.0:3000"]
