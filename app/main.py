from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app import models, crud, auth, database
from app.routers import posts, users, pages
import os

app = FastAPI(title="Blogging Website", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(pages.router)

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(auth.get_db)):
    posts = crud.get_posts(db)
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})
