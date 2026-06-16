from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import crud, auth, schemas
from app.auth import get_db
import markdown

router = APIRouter(prefix="/posts", tags=["posts"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/new", response_class=HTMLResponse)
async def create_post_form(request: Request):
    return templates.TemplateResponse("create_post.html", {"request": request})

@router.post("/new")
async def create_post(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    # For demo, using user_id=1 (you should get from session)
    post = schemas.PostCreate(title=title, content=content)
    crud.create_post(db, post, author_id=1)
    return RedirectResponse("/", status_code=303)

@router.get("/{post_id}", response_class=HTMLResponse)
async def read_post(request: Request, post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.content_html = markdown.markdown(post.content)
    return templates.TemplateResponse("post_detail.html", {"request": request, "post": post})
