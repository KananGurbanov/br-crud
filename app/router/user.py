from typing import Optional

from fastapi import APIRouter, Depends

from app.db.db_initializer import get_session
from app.dtos.user import UserCreate, UserRetrieve
from app.mapper.user import UserMapper
from app.service.user import user_service

user_router = APIRouter()



@user_router.post("/",  response_model=UserRetrieve)
def create(source: UserCreate):
    with get_session() as session:
        return user_service.create(user=source, session=session)


@user_router.delete("/{user_id}")
def delete(user_id: int):
    with get_session() as session:
        user_service.delete_by_id(user_id=user_id, session=session)


@user_router.get("/{user_id}", response_model=UserRetrieve)
def get_by_id(user_id: int):
    with get_session() as session:
        return user_service.find_by_id(user_id=user_id, session=session)


@user_router.get("")
def search(search_term: Optional[str] = None):
    with get_session() as session:
        return user_service.search(search_term=search_term, session=session)