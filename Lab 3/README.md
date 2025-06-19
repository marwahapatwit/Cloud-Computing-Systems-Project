# Lab 3 — FastAPI + Uvicorn Application

---

## Description

The application includes:

- A FastAPI server (`main.py`)
- 15+ routes using GET and PUT methods
- A combination of:
  - Query String Parameters
  - Path Parameters
  - Request Body Inputs
- A Python script (`driver.py`) that programmatically accesses and tests each route

---

## Design

- **main.py**: The core FastAPI app with endpoints such as `/greet`, `/event/{event_name}`, and `/rsvp`.
- **driver.py**: A simple test client using the `requests` module to call the routes and print results.
- **Uvicorn**: Lightweight ASGI server to serve the app.
- **Swagger UI**: Interactive documentation is automatically generated at `/docs`.

---

## Detailed Instructions to Run the Project

### Step 1: Set up your environment 

If not already activated:
```bash
cd "Lab 3"
python -m venv venv
venv\Scripts\activate  # For Windows

### Step 2: Install Dependencies

pip install fastapi uvicorn requests

### Step 3: Run the FastAPI Server

uvicorn main:app --reload

### Step 4: Open In Browser

Hello route: http://127.0.0.1:8000/

Swagger docs: http://127.0.0.1:8000/docs

### Step 5: Run The Python Driver

python driver.py