
FROM python:3.10

WORKDIR /app

# Copy all files including seed_token.py
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command: Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]
