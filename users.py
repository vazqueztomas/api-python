from fastapi import FastAPI, HTTPException
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


@app.post("/user/", response_model=User, status_code=201)
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users.append(user)
    return user


@app.put("/user/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users):
        if saved_user.id == user.id:
            users[index] = user
            found = True
            return user
    if not found:
        raise HTTPException(
            status_code=404, detail="No se ha encontrado al usuario")


@app.delete("/user/{id}")
async def user(id: int):
    for index, saved_user in enumerate(users):
        if saved_user.id == id:
            del users[index]


def search_user(id: int):
    usuarios = filter(lambda user: user.id == id, users)
    try:
        return list(usuarios)[0]
    except:
        raise HTTPException(
            status_code=404, detail="No se ha encontrado al usuario")
