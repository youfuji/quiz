from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# 静的ファイル (auth.js) を提供する
app.mount("/frontend/static", StaticFiles(directory=os.path.abspath("../frontend/static")), name="static")

# フォームの表示 (GET)
@app.get("/", response_class=HTMLResponse)
async def get_form():
    file_path = os.path.abspath(os.path.join("..", "frontend", "templates", "index.html"))
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# auth.html の表示 (GET)
@app.get("/auth", response_class=HTMLResponse)
async def auth_page():
    file_path = os.path.abspath(os.path.join("..", "frontend", "templates", "auth.html"))
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# quiz_add.html の表示 (GET)
@app.get("/add", response_class=HTMLResponse)
async def add_page():
    file_path = os.path.abspath(os.path.join("..", "frontend", "templates", "quiz_add.html"))
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# フォームデータの送信 (POST)
@app.post("/submit")
async def submit_form(name: str = Form(...), password: str = Form(...)):
    return RedirectResponse(url="/", status_code=302)