
# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /mutant_app

# Install dependencies
COPY /mutant_app /mutant_app /
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Start FastAPI application
CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "8000"]
