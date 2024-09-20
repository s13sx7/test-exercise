from fastapi import FastAPI
from app.Users.router import router as router_users
app = FastAPI()

app.include_router(router_users)