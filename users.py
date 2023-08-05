from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    isDeveloper: bool


users = [User(name="Tomas", age=21, isDeveloper=True),
         User(name="Manuel", age=23, isDeveloper=False)]


@app.get('/')
async def get_users():
    return {"users": users}
