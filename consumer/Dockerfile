FROM python:3.9

WORKDIR /app
COPY consumer.py .

RUN pip install requests

CMD ["python", "consumer.py"]