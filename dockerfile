# Use official slim Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your app code into the container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir numpy pandas scikit-learn

# Run your Python app
CMD ["python", "main.py"]
