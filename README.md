
# System Health Reporter

## Overview
System Health Reporter is a Python-based CLI tool developed as part of the **Atomixtools Software Developer Intern assignment**.

The tool collects system health metrics such as **CPU usage**, **memory usage**, and **disk usage**, and displays the results in a structured **JSON format**.  
The project is fully **Dockerized** for easy execution across environments.

---

## Features
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- JSON formatted output
- Optional verbose mode
- Docker support

---

## Tech Stack
- Python 3
- Docker
- Git & GitHub

---
## Project Structure

```text
system-health-reporter/
├── app/
│   └── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

### File Description
- `app/main.py` – Main Python script that collects and prints system health metrics  
- `Dockerfile` – Instructions to build the Docker image  
- `requirements.txt` – Python dependencies  
- `README.md` – Project documentation  

---

## Prerequisites
Make sure the following are installed:
- Python 3.8 or higher
- Docker
- Git

---

## Run Locally (Without Docker)

### 1. Clone the repository

```bash

git clone git@github.com:manvithareddyk/system-health-reporter.git
cd system-health-reporter
```
### 2.Install Dependencies
```bash
pip install -r requirements.txt
```
### 3.Run the Application
```bash
python app/main.py
```
### 4.Run in Verbose mode
```bash
python app/main.py --verbose
```
## Run using Docker
### 1. Build the Docker image
``` bash
docker build -t system-health-reporter .
```
### 2.Run the Docker contaner using built image
``` bash
docker run system-health-reporter
```
## Output Format
``` text
{
  "cpu_usage": "15%",
  "memory_usage": "45%",
  "disk_usage": "60%"
}
```





