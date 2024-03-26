# Use a slim Python base image
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy just the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run on container start
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]

