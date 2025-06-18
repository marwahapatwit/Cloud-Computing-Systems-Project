from fastapi import FastAPI, Path, Query, Body

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI"}

# GET routes 
@app.get("/greet")
def greet(name: str = Query(...)):
    return {"message": f"Hello, {name}!"}

@app.get("/square")
def square(num: int = Query(...)):
    return {"result": num ** 2}

@app.get("/temperature")
def convert_temp(celsius: float = Query(...)):
    return {"fahrenheit": (celsius * 9/5) + 32}

@app.get("/search")
def search_events(keyword: str = Query(...)):
    return {"result": f"Searching events for '{keyword}'"}

@app.get("/multiply")
def multiply(a: int = Query(...), b: int = Query(...)):
    return {"product": a * b}

# GET routes
@app.get("/user/{user_id}")
def get_user(user_id: int = Path(...)):
    return {"user_id": user_id}

@app.get("/event/{event_name}")
def event_details(event_name: str = Path(...)):
    return {"event": event_name, "status": "active"}

@app.get("/pillars/{pillar}")
def get_pillar(pillar: str = Path(...)):
    return {"pillar_info": f"{pillar} is a core part of Blankhouse."}

@app.get("/year/{year}")
def get_by_year(year: int = Path(...)):
    return {"message": f"Showing events from {year}"}

@app.get("/item/{category}/{id}")
def get_item(category: str, id: int):
    return {"category": category, "item_id": id}

# PUT routes
@app.put("/submit-feedback")
def feedback(data: dict = Body(...)):
    return {"received": data}

@app.put("/update-user")
def update_user(user: dict = Body(...)):
    return {"status": "user updated", "user": user}

@app.put("/event-update")
def update_event(event: dict = Body(...)):
    return {"event": event, "status": "update received"}

@app.put("/join-waitlist")
def waitlist(entry: dict = Body(...)):
    return {"message": "Added to waitlist", "entry": entry}

@app.put("/rsvp")
def rsvp(info: dict = Body(...)):
    return {"response": "RSVP confirmed", "details": info}
