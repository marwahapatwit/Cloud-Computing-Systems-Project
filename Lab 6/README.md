# Lab 6 - FastAPI Back-End for Guitar Database

## Introduction
This project creates a FastAPI-based back-end for interacting with a simplified guitar product database.

## Description
It includes 10 routes using both GET and PUT methods to simulate CRUD operations and filtering over guitar products.

## Design
The system uses:
- Python 3
- FastAPI framework
- Uvicorn as the ASGI server
- In-memory database (dictionary) to mock real data

## How to Run

1. Install dependencies:
```bash
pip install fastapi uvicorn
```

2. Run the server:
```bash
uvicorn main:app --reload
```

3. Access the API docs at:
```
http://127.0.0.1:8000/docs
```