from fastapi import HTTPException

from app.constants.phone import AZERBAIJAN_MOBILE_PREFIXES


def is_valid_length(phone_number: str) -> bool:
    return len(phone_number) == 10


def has_valid_prefix(phone_number: str, prefixes: list) -> bool:
    return any(phone_number.startswith(prefix) for prefix in prefixes)


def is_valid_mobile_number(phone_number: str) -> bool:
    return is_valid_length(phone_number) and has_valid_prefix(phone_number, AZERBAIJAN_MOBILE_PREFIXES)



def validate_phone_number(phone: str):
    if not is_valid_mobile_number(phone):
        raise _build_exception()


def _build_exception() -> HTTPException:
    return HTTPException(status_code=400, detail="Invalid Azerbaijan mobile number.")