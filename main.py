from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "First API with FastApi"


@app.get('/url')
async def get_url():
    return {"url": "tomasvazquez.web.app/"}
