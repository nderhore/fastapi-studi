from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.config.database import get_db
from src.controller.movie_controller import create_movie, read_movies, read_movie, update_movie, delete_movie
from src.schema.movie_schema import MovieResponse, MovieCreate


class MovieAPI:
    def __init__(self):
        self.router = APIRouter()
        self.add_routes()

    def add_routes(self):
        @self.router.post("/", response_model=MovieResponse)
        def create_movie_endpoint(movie: MovieCreate, db: Session = Depends(get_db)):
            return create_movie(movie, db)

        @self.router.get("/", response_model=List[MovieResponse])
        def read_movies_endpoint(db: Session = Depends(get_db)):
            return read_movies(db)

        @self.router.get("/{movie_id}", response_model=MovieResponse)
        def read_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
            return read_movie(movie_id, db)

        @self.router.put("/{movie_id}", response_model=MovieResponse)
        def update_movie_endpoint(movie_id: int, updated_movie: MovieCreate, db: Session = Depends(get_db)):
            return update_movie(movie_id, updated_movie, db)

        @self.router.delete("/{movie_id}", response_model=MovieResponse)
        def delete_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
            return delete_movie(movie_id, db)
