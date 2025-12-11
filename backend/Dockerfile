# Backend Dockerfile (Django + Waitress)
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# Use waitress inside container (works on Windows and Linux)
CMD ["waitress-serve", "--listen=0.0.0.0:8080", "core.wsgi:application"]