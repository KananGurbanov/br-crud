from fastapi import FastAPI

from app.db.db_initializer import create_tables, get_session
from app.router.user import user_router

app = FastAPI()

create_tables()

app.include_router(user_router, prefix="/users", tags=["Users Router"])

@app.get("/health")
async def healthcheck(name: str):
    return {"status": "healthy"}
