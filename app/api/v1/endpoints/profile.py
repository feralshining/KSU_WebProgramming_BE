from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/profiles", tags=["profiles"])

class Profile(BaseModel):
    animal: str
    name: str
    age: int

# Mock data
profiles = {
    "dog": {"animal": "dog", "name": "Buddy", "age": 3},
    "cat": {"animal": "cat", "name": "Whiskers", "age": 2},
}

@router.get("/{animal}")
def get_profile(animal: str):
    profile = profiles.get(animal.lower())
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile