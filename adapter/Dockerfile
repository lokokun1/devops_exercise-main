FROM python:3.12-slim

WORKDIR /app
RUN pip install --no-cache-dir flask requests

COPY app.py /app/app.py
EXPOSE 8001

CMD ["python3", "app.py"]
