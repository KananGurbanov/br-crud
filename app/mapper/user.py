from app.dtos.user import UserCreate, UserRetrieve
from app.models.user import User


class UserMapper:
    @staticmethod
    def to_entity(source: UserCreate) -> User:

        result = User(
            name=source.firstname,
            lastname=source.lastname,
            phone_number=source.phone_number,
            process_case=source.process_case,
            text=source.text
        )
        return result

    @staticmethod
    def to_dto(user: User) -> UserRetrieve:
        return UserRetrieve(
            id=user.id,
            firstname=user.name,
            lastname=user.lastname,
            phone_number=user.phone_number,
            process_case=user.process_case,
            text=user.text
        )
