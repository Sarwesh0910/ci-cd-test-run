# CI/CD Pipeline with SonarQube + Docker

This project demonstrates a full CI/CD pipeline using Jenkins, SonarQube, Docker, and GitHub.

## Features
- Flask app with health endpoint
- Unit tests with Pytest
- SonarQube code quality analysis
- Docker image build and push to DockerHub
- Jenkins pipeline with webhook trigger
- Role-based access control in Jenkins

## Endpoints
- `/` → Hello World
- `/health` → OK

## Setup
1. Clone repo
2. Configure Jenkins and SonarQube
3. Set DockerHub credentials in Jenkins
4. Trigger build via GitHub webhook
