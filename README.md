# DevOps-Containerised-Web-App
A containerised web application project showcasing DevOps workflows, Docker-based deployment, and automated CI/CD pipelines.

This project demonstrates how to build and run a multi-container backend application using Docker.
The application uses a Flask API, PostgreSQL database, and an Nginx reverse proxy, all orchestrated using Docker Compose.

The goal of this project is to understand containerization, service orchestration, and container networking in a DevOps workflow.


Architecture

The system follows a simple backend architecture:

User
 │
 ▼
Nginx (Reverse Proxy)
 │
 ▼
Flask API (Python)
 │
 ▼
PostgreSQL Database

Request Flow
	1.	User sends a request to the server
	2.	Nginx receives the request
	3.	Nginx forwards the request to the Flask API
	4.	Flask processes the request
	5.	Flask communicates with PostgreSQL if database data is required
	6.	Response is returned to the user

Tech Stack
	•	Python (Flask)
	•	PostgreSQL
	•	Nginx
	•	Docker
	•	Docker Compose

Project Structur

devops-containerised-web-app
│
├── app
│   ├── app.py
│   └── requirements.txt
│
├── nginx
│   └── default.conf
│
├── Dockerfile
├── docker-compose.yml
└── README.md

Containers

The project runs three containers:
	•	nginx_proxy → Reverse proxy server
	•	flask_app → Backend API service
	•	postgres_db → PostgreSQL database

Check running containers:

Bash
docker ps

API Endpoints

Root Endpoint
GET /

Response: DevOps Project Running by Nitin Raut

Health Check
GET /health

Health Check: Service is healthy

Database Test
Bash
GET /db

This endpoint connects to PostgreSQL and returns the database version.

Example response: PostgreSQL version: PostgreSQL 18.x

What This Project Demonstrates
	•	Containerizing applications using Docker
	•	Running multi-container systems with Docker Compose
	•	Reverse proxy architecture using Nginx
	•	Container-to-container networking
	•	Connecting a backend service to a database

Future Improvements

Possible improvements for this project:
	•	Persistent database storage using Docker volumes
	•	Container health checks
	•	Logging and monitoring
	•	CI/CD pipeline using GitHub Actions
	•	Load balancing with multiple API containers


Author

Nitin Raut
DevOps Learning Project
