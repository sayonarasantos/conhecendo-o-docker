from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    director: str
    genre: str
    year: int

    class Config:
        orm_mode = True
