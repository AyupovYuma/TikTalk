from fastapi import FastAPI
from app.core.session import init_db
from app.routers import auth
app = FastAPI()

init_db()

app.include_router(auth.router)