FROM python:3.8.10-slim

WORKDIR /app

COPY ./api_yamdb/ .

RUN pip3 install -r requirements.txt --no-cache-dir
RUN mkdir static
RUN mv ./redoc.yaml static/

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
