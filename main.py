from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# Routers
app.include_router(products.router)
app.include_router(users.router)

app.mount('/static', StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return "First API with FastApi"


@app.get('/url')
async def get_url():
    return {"url": "tomasvazquez.web.app/"}
