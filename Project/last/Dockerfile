FROM python:3.12-slim
WORKDIR /app
COPY app.py .
COPY requirements.txt . 
RUN pip install -r requirements.txt
EXPOSE 5003
CMD flask run --host=0.0.0.0 --port=5003