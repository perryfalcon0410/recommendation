from fastapi import FastAPI
from server.routes.user import user

app = FastAPI()
app.include_router(user)
