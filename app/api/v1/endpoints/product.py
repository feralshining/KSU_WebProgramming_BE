from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["products"])

class Product(BaseModel):
    id: int
    name: str
    description: str

# Mock data
products = [
    {"id": 1, "name": "Product 1", "description": "Description 1"},
    {"id": 2, "name": "Product 2", "description": "Description 2"},
]

@router.get("/{productId}")
def get_product(productId: int):
    product = next((p for p in products if p["id"] == productId), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product