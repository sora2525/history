import uuid

from ulid import ULID


def generate_ulid() -> str:
    return str(ULID())


def generate_uuidv4() -> str:
    return str(uuid.uuid4())