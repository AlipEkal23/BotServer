FROM docker:20
FROM ubuntu:latest

# Install Docker
RUN apt-get update && \
    apt-get install -y docker.io

# Rest of your Dockerfile
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]
