from fastapi import FastAPI, Header, Cookie, Response, HTTPException

app = FastAPI()

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="session_id", value="abc123", httponly=True)
    return {"message": "Cookie set"}

@app.get("/get-cookie")
def get_cookie(session_id: str = Cookie(default=None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="No session cookie found")
    return {"session_id": session_id}

@app.get("/check-user-agent")
def check_user_agent(user_agent: str = Header(default=None)):
    return {"user_agent": user_agent}

@app.get("/custom-header")
def custom_header(x_custom_token: str = Header(default=None)):
    if not x_custom_token:
        raise HTTPException(status_code=401, detail="Missing X-Custom-Token header")
    return {"X-Custom-Token": x_custom_token}

@app.get("/full-info")
def full_info(user_agent: str = Header(default=None), session_id: str = Cookie(default=None)):
    return {
        "user_agent": user_agent,
        "session_id": session_id or "not set"
    }