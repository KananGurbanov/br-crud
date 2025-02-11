from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    text: Optional[str] = None
    process_case: Optional[str] = None

class UserRetrieve(BaseModel):
    id: int
    firstname: str
    lastname: str
    phone_number: str
    text: Optional[str] = None
    process_case: Optional[str] = None

