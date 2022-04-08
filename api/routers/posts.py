from fastapi import APIRouter, status

from database import post_collection


router = APIRouter(prefix="/posts", tags=["heroes"])

@router.get("/{owner}", status_code=status.HTTP_200_OK)
def get_post(owner: str) -> dict:
    return post_collection.get_post({'owner': owner})
