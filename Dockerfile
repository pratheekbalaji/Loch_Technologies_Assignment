FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py /app

CMD ["python3", "./app.py"]
