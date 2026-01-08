from fastapi import FastAPI
from app.routes import content

app = FastAPI(title="AutoProfit Content Empire")
app.include_router(content.router, prefix="/api/content")
