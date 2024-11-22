from pydantic import BaseModel


class OwnerSchema(BaseModel):
    fullname: str
    document: str

