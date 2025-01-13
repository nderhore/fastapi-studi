from fastapi import FastAPI

from api.api import MovieAPI
from src.config.database import Base, engine

# Création des tables
Base.metadata.create_all(bind=engine)

# Création de l'application FastAPI
app = FastAPI()

# Initialisation de l'API Movie
movie_api = MovieAPI()

# Montage des routes de MovieAPI
app.include_router(movie_api.router, prefix="/movies", tags=["Movies"])
