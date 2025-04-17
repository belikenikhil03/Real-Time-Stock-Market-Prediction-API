# Use a lightweight Python 3.9 image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt .

# Install dependencies without caching pip files
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to the working directory
COPY . .

# Run the Flask app
CMD ["python", "app.py"]