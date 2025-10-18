# HNG Stage 0 Backend Task - Dynamic Profile Endpoint

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A RESTful API built with FastAPI that returns dynamic profile information along with random cat facts fetched from an external API. This project is part of the HNG Internship Stage 0 Backend task.

## 🚀 Live Demo

**API Endpoint:** [https://hng-0-pspzoq.fly.dev/me](https://hng-0-pspzoq.fly.dev/me)

**Interactive API Documentation (Swagger UI):** [https://hng-0-pspzoq.fly.dev/docs](https://hng-0-pspzoq.fly.dev/docs)

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)

## ✨ Features

- **Dynamic Profile Data**: Returns user profile information with real-time UTC timestamp
- **Cat Facts Integration**: Fetches random cat facts from the Cat Facts API on every request
- **Error Handling**: Graceful error handling with fallback mechanisms
- **Auto-Documentation**: Interactive Swagger UI for API testing
- **ISO 8601 Timestamps**: Standardized datetime format for consistency
- **Production Ready**: Deployed on Fly.io with proper configuration

## 📁 Project Structure

```
hng_0/
│
├── src/
│   ├── __init__.py          # Package initialization
│   ├── routes.py            # API route definitions
│   ├── schemas.py           # Pydantic models for request/response validation
│   └── services.py          # Business logic and external API integration
│
├── .gitignore              # Git ignore file
├── Dockerfile              # Docker configuration for deployment
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🛠️ Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern, fast web framework for building APIs
- **[Python 3.8+](https://www.python.org/)**: Programming language
- **[Uvicorn](https://www.uvicorn.org/)**: ASGI server for running FastAPI applications
- **[Pydantic](https://docs.pydantic.dev/)**: Data validation using Python type hints
- **[httpx](https://www.python-httpx.org/)**: Async HTTP client for external API calls
- **[Fly.io](https://fly.io/)**: Deployment platform

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/Anjola11/hng_0.git
cd hng_0
```

2. **Create a virtual environment** (recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## 🚀 Running Locally

### Method 1: Using Uvicorn (Recommended)

```bash
uvicorn src:app --reload
```

The API will be available at:
- **Base URL**: http://127.0.0.1:8000
- **Endpoint**: http://127.0.0.1:8000/me
- **Swagger Docs**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### Method 2: Using Python directly

```bash
python -m uvicorn src:app --reload
```

### Method 3: Custom host and port

```bash
uvicorn src:app --reload --host 0.0.0.0 --port 8080
```

## 📖 API Documentation

### GET `/me`

Returns profile information with a dynamic cat fact.

#### Response Format

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "A random cat fact from the Cat Facts API"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Always returns "success" |
| `user.email` | string | Developer's email address |
| `user.name` | string | Developer's full name |
| `user.stack` | string | Backend technology stack |
| `timestamp` | string | Current UTC time in ISO 8601 format |
| `fact` | string | Random cat fact fetched from external API |

#### Example Request

```bash
curl -X GET "https://hng-0-pspzoq.fly.dev/me"
```

#### Example Response

```json
{
  "status": "success",
  "user": {
    "email": "aladeniyiaanu@example.com",
    "name": "Aladeniyi Aanu",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T07:24:15.123Z",
  "fact": "Cats have over 20 vocalizations, including the purr, meow, and hiss."
}
```

#### Status Codes

- `200 OK`: Successful response
- `500 Internal Server Error`: Server error or external API failure
- `503 Service Unavailable`: Cat Facts API is temporarily unavailable

## 🌐 Deployment

This project is deployed on **Fly.io**. The deployment process uses Docker for containerization.

### Deployment Steps

1. Install Fly CLI
2. Login to Fly.io: `fly auth login`
3. Deploy: `fly deploy`

The `Dockerfile` in the repository handles the containerization process.

## ⚠️ Error Handling

The API implements graceful error handling:

- **External API Failures**: If the Cat Facts API is unavailable, a fallback message is returned
- **Network Timeouts**: Requests to external API have a timeout configured
- **Validation Errors**: Pydantic models ensure data integrity

## 🧪 Testing

### Manual Testing

1. **Test locally**:
   ```bash
   curl http://127.0.0.1:8000/me
   ```

2. **Test deployed version**:
   ```bash
   curl https://hng-0-pspzoq.fly.dev/me
   ```

3. **Use Swagger UI**:
   Visit http://127.0.0.1:8000/docs and test interactively



**Note**: This project was created as part of the HNG Internship Stage 0 Backend task. 
