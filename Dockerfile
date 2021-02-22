FROM python:3.9.0

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv install --system --deploy --ignore-pipfile

EXPOSE 80

COPY ./poc /poc

WORKDIR /poc

CMD ["gunicorn", "--workers=10", "--bind=0.0.0.0:80", "poc.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]