from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbit'
        from_attributes = True