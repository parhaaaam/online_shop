# Dockerfile
FROM python:3.12-alpine

RUN pip install Flask mysql-connector-python

WORKDIR /app

COPY ./ /app/

EXPOSE 5000

CMD ["python3", "./complex_queries.py"]
