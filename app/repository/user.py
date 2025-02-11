from typing import Optional

from sqlalchemy import or_, String
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def save(self, session: Session, user: User) -> User:
        session.add(user)
        session.commit()
        return user

    def delete_by_id(self, user_id: int, session: Session):
        session.delete(session.query(User).filter(User.id == user_id).first())
        session.commit()

    def find_by_id(self, user_id: int, session: Session):
        return session.query(User).filter(User.id == user_id).first()

    def search(self, search_term: Optional[str], session: Session):
        if search_term:
            search_pattern = f"%{search_term}%"
            filtered_query = session.query(User).filter(
                or_(
                    User.name.ilike(search_pattern),
                    User.lastname.ilike(search_pattern),
                )
            )

            return filtered_query.all()

        else:
            return session.query(User).all()


user_repository = UserRepository()
