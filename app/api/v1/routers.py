from fastapi import APIRouter
from .endpoints.main import router as main_router
from .endpoints.product import router as product_router
from .endpoints.profile import router as profile_router

api_router = APIRouter()
api_router.include_router(main_router)
api_router.include_router(product_router)
api_router.include_router(profile_router)