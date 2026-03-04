from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine, Base
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"db_response": result.scalar()}
