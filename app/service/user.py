from typing import List, Optional

from fastapi import HTTPException
from injector import inject
from sqlalchemy.orm import Session

from app.dtos.user import UserCreate, UserRetrieve
from app.mapper.user import UserMapper
from app.repository.user import UserRepository, user_repository
from app.utility.phone import validate_phone_number


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, user: UserCreate, session: Session) -> UserRetrieve:
        if user.phone_number:
            validate_phone_number(user.phone_number)
        user = UserMapper.to_entity(user)
        user = self.user_repository.save(user=user, session=session)
        return UserMapper.to_dto(user)

    def delete_by_id(self, user_id: int, session: Session):
        self.user_repository.delete_by_id(user_id=user_id, session=session)


    def find_by_id(self, user_id: int, session: Session) -> UserRetrieve:
        user = self.user_repository.find_by_id(user_id=user_id, session=session)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserMapper.to_dto(user)

    def search(self, search_term: Optional[str], session: Session) -> List[UserRetrieve]:
        return self.user_repository.search(search_term=search_term, session=session)




user_service = UserService(user_repository=user_repository)
