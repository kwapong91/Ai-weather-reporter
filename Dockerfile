FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Creating a non-root user
RUN useradd -m admin
USER admin

# Expose the port the app runs on
EXPOSE 5003

# Run the application
CMD ["python", "main.py"]