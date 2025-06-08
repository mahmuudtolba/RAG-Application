from fastapi import FastAPI , APIRouter
import os





base_router = APIRouter(
    prefix = "/api/v1",
    tags=['api_v1']
)

@base_router.get("/")
async def home():
    # Access the environment variables
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION") 

    return {"APP_NAME" : APP_NAME ,
            "APP_VERSION" : APP_VERSION}