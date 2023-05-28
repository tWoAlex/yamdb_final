FROM python:3.8.10-slim

WORKDIR /app

COPY ./ .

RUN python -m pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
