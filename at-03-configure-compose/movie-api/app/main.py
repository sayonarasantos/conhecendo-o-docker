import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.schema import Movie as SchemaMovie
from app.schema import Movie
from app.models import Movie as ModelMovie
from app.config import DATABASE_URL


app = FastAPI()


app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

@app.get("/")
async def root():
    return {"message": "Movie API"}


@app.post('/movie/', response_model=SchemaMovie)
async def movie(movie: SchemaMovie):
    db_movie = ModelMovie(title=movie.title, director=movie.director, genre=movie.genre, year=movie.year)
    db.session.add(db_movie)
    db.session.commit()
    return db_movie

@app.get('/movie/')
async def movie():
    movie = db.session.query(ModelMovie).all()
    return movie
