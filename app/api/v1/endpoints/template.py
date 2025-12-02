from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from flask import app

app = FastAPI()

template = Jinja2Templates(directory="app/api/v1/endpoints")

@app.get("/",  response_class = HTMLResponse)
async def read_root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/result", response_class = HTMLResponse)
async def post_result(
    request: Request,
    content: str = Form(...)
):
    return template.TemplateResponse("result.html", {"request": request, "content": content})


