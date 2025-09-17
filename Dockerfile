FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install FastAPI and uvicorn (missing from requirements.txt)
RUN pip install --no-cache-dir fastapi uvicorn

# Copy application code
COPY . .

# Create outputs directory
RUN mkdir -p outputs

# Expose port for FastAPI
EXPOSE 8000

# Default command runs FastAPI server
CMD ["python", "main.py"]