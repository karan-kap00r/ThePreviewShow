from fastapi import FastAPI
from app.routes import preview, upload

app = FastAPI()

app.include_router(preview.router, prefix="/preview")
app.include_router(upload.router, prefix="/upload")

@app.get("/")
async def home():
    return {"message": "Welcome to the Content Preview API"}
