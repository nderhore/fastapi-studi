from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from src.model.movie import Movie
from src.schema.movie_schema import MovieCreate


# Créer un film
def create_movie(movie: MovieCreate, db: Session):
    db_movie = Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# Lire tous les films
def read_movies(db: Session):
    return db.query(Movie).all()

# Lire un film par ID
def read_movie(movie_id: int, db: Session):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# Mettre à jour un film
def update_movie(movie_id: int, updated_movie: MovieCreate, db: Session):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in updated_movie.dict().items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie

# Supprimer un film
def delete_movie(movie_id: int, db: Session):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return movie
