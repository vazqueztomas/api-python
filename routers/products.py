from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products")


products_list = ["Producto1", "Producto2", "Producto3"]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    if id > len(products_list):
        raise HTTPException(404, detail="No se encuentra el producto.")

    return products_list[id]
