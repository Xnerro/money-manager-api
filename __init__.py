from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from src import *
from src.endpoint.main import route

app = FastAPI(title="My Money Manager", description="Manage money our money flow from website", version="1.0.0")


app.include_router(route)
