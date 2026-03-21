# DevOps-Containerised-Web-App

A containerised web application project showcasing DevOps workflows, Docker-based deployment, and multi-container architecture using Docker Compose.

---

## Project Overview

This project demonstrates how to build and run a backend system using:

- Flask API (Python)
- PostgreSQL Database
- Nginx Reverse Proxy
- Docker & Docker Compose

The focus is on:
- Containerization
- Service orchestration
- Container networking
- Data persistence using volumes

---

## Architecture

User  
↓  
Nginx (Reverse Proxy)  
↓  
Flask API  
↓  
PostgreSQL Database  

---

## Request Flow

1. User sends request to server  
2. Nginx receives request  
3. Nginx forwards request to Flask  
4. Flask processes request  
5. Flask connects to PostgreSQL  
6. Response is returned  

---

## Tech Stack

- Python (Flask)
- PostgreSQL
- Nginx
- Docker
- Docker Compose

---

## Project Structure

devops-containerised-web-app

├── app  
│   ├── app.py  
│   └── requirements.txt  

├── nginx  
│   └── default.conf  

├── Dockerfile  
├── docker-compose.yml  
└── README.md  

---

## Containers

- nginx_proxy → Reverse proxy  
- flask_app → Backend API  
- postgres_db → Database  

---

## How to Run

Start:
docker compose up -d

Stop:
docker compose down

Check running:
docker ps

---

## API Endpoints

GET /
→ DevOps Project Running by Nitin Raut

GET /health
→ Service is healthy

GET /db
→ Returns PostgreSQL version

---

## Data Persistence (NEW)

This project uses Docker volumes:

postgres_data → /var/lib/postgresql/data

Why this is important:
- Data is not lost after container stop
- Database survives restart
- Real-world production behavior

---

## Persistence Test (What we did)

1. Start containers:
docker compose up -d

2. Test DB:
curl http://localhost:8080/db

3. Stop:
docker compose down

4. Start again:
docker compose up -d

5. Test again:
curl http://localhost:8080/db

Result:
Database still works → Data persisted

---

## Networking

- Flask connects to DB using:
DB_HOST=db

- Nginx forwards to:
http://app:5000

---

## What This Project Demonstrates

- Docker containerization  
- Multi-container setup  
- Nginx reverse proxy  
- Service communication  
- PostgreSQL integration  
- Persistent storage using volumes  

---

## Future Improvements

- Add health checks  
- Use Gunicorn (production server)  
- Add logging & monitoring  
- CI/CD with GitHub Actions  
- Load balancing  

---

## Author

Nitin Raut  
DevOps Learning Project
