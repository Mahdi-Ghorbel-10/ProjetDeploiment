from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

# Include routes
app.include_router(router)
