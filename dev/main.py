from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import sqlite3

conn = sqlite3.connect("mydatabase.db")
c = conn.cursor()

import logging

logging.basicConfig(level=logging.DEBUG)

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
""")

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/signup")
async def signup_post(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    create_user(name, email, password)
    return RedirectResponse(url="/users")


@app.get("/users", response_class=HTMLResponse)
async def users(request: Request):
    users = get_users()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/signin", response_class=HTMLResponse)
async def signin(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


@app.post("/signin")
async def signin(request: Request, username: str, password: str):
    # check if user exists in the database
    c.execute("SELECT * FROM users WHERE name=? AND password=?", (username, password))
    user = c.fetchone()
    if user:
        # redirect to home page after successful sign in
        response = RedirectResponse(url="/home")
        return response
    else:
        return templates.TemplateResponse("signin.html", {"request": request, "error": "Invalid username or password"})



def create_user(name: str, email: str, password: str):
    try:
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
    except Exception as e:
        
        print(f"Error creating user: {e}")


def get_users():
    c.execute("SELECT name, email FROM users")
    users = c.fetchall()
    return users


def authenticate_user(email: str, password: str):
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()
    return user
