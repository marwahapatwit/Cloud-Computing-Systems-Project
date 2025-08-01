# Lab 7 – FastAPI Headers and Cookies

## Introduction
This lab implements a FastAPI service demonstrating usage of request headers and cookies.

## Description
The service defines 5 routes using FastAPI's `Header` and `Cookie` dependencies to simulate session-based and token-based request flows.

## Routes Implemented
1. `GET /set-cookie` – sets a session cookie
2. `GET /get-cookie` – reads the session cookie
3. `GET /check-user-agent` – extracts and returns the User-Agent header
4. `GET /custom-header` – reads a custom header (X-Custom-Token)
5. `GET /full-info` – combines User-Agent header and session cookie

## Design
- Framework: FastAPI
- Server: Uvicorn
- No database – session data simulated via cookies

## How to Run

1. Install dependencies:
```bash
pip install fastapi uvicorn
```

2. Run the server:
```bash
uvicorn main:app --reload
```

3. Test via browser or Postman:
- Use `/set-cookie` first to create a cookie
- Access `/get-cookie`, `/custom-header`, etc. with appropriate headers and cookies