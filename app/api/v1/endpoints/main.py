from fastapi import APIRouter

router = APIRouter(tags=["main"])

@router.get("/")
def get_main():
    return {"message": "Welcome to the API"}