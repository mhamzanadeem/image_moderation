from fastapi import FastAPI
from auth import router as auth_router
from moderation import router as mod_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(mod_router)
