FROM python:3.9

WORKDIR /app
COPY producer.py .

RUN pip install flask

CMD ["python", "producer.py"]