# Use official Python base image
FROM python:3.8-slim

# Set working directory in container
WORKDIR /app

# Copy requirements.txt first to install dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on (adjust if needed)
EXPOSE 8000

# Command to run your app:
# For Django (adjust if your manage.py is in a subfolder):
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# For Flask (if your app entry point is app.py):
# CMD ["python", "app.py"]

# Replace the line below with your app's start command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
