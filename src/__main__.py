from fastapi import FastAPI
from routes import owner_router
from models import Base
from db import db_connection



app = FastAPI()

app.include_router(owner_router)


if __name__ == "__main__":
    import uvicorn
    Base.metadata.create_all(bind=db_connection.engine)
    uvicorn.run(app, host='localhost', port=8080)

