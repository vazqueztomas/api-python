from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int
    isDeveloper: bool


users = [User(id=1, name="Tomas", age=21, isDeveloper=True),
         User(id=2, name="Manuel", age=23, isDeveloper=False)]


@app.get('/')
async def get_users():
    return {"users": users}


@app.get('/user/{id}')
async def get_user_by_id(id: int):
    return search_user(id)


@app.get("/userquery/")
async def get_user_by_query(id: int):
    return search_user(id)


@app.post("/user/")
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users.append(user)
        return {"Usuario agregado": user}


def search_user(id: int):
    usuarios = filter(lambda user: user.id == id, users)
    try:
        return list(usuarios)[0]
    except:
        return {"error": "No se ha encontrado al usuario"}
