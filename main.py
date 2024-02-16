## Author : ARUNKUMAAR R
## Description : Creating Main Python file
## Date : 16/02/24
## Language : PYTHON

#uvicorn main:app --reload
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="/code")

@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})
