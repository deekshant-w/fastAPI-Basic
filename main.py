from fastapi import FastAPI
from image import image
from text import text
from crud import main as crud

app = FastAPI()

app.include_router(
    image.app,
    prefix="/image",
    tags=["Image Functions"],
)

app.include_router(
    text.router,
    prefix="/text",
    tags=["Text Functions"],
)

app.include_router(
    crud.router,
    prefix="/crud",
    tags=["CRUD Functions"],
)