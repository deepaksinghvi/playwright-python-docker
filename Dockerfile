# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN apt-get update && \
    apt-get install -y libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxcomposite1 libxrandr2 libxdamage1 libxkbcommon0 libpango-1.0-0 libxshmfence1 libgbm1 && \
    pip install --no-cache-dir playwright && \
    playwright install --with-deps

# Copy the rest of the application code
COPY . .

# Command to run the Python script
CMD ["python", "test_script.py"]

