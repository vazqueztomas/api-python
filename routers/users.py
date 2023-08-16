from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/user", tags=["Users"])


class User(BaseModel):
    id: int
    name: str
    age: int
    isDeveloper: bool


users = [User(id=1, name="Tomas", age=21, isDeveloper=True),
         User(id=2, name="Manuel", age=23, isDeveloper=False)]


@router.get('/')
async def get_users():
    return {"users": users}


@router.get('/{id}')
async def get_user_by_id(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=201)
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users.routerend(user)
    return user


@router.put("/")
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


@router.delete("/{id}")
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
