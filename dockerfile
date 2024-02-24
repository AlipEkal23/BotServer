FROM docker:20-dind

# Install additional dependencies
RUN apk add --no-cache python3 python3-dev py3-pip build-base

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run your application
CMD ["python3", "your_bot_script.py"]
