import os

from fastapi import FastAPI

from api.movie_api import MovieAPI
from api.auth_api import router as auth_router
from src.config.database import Base, engine
import uvicorn

# Création des tables
Base.metadata.create_all(bind=engine)

# Création de l'application FastAPI
app = FastAPI()

# Initialisation de l'API Movie
movie_api = MovieAPI()

# Montage des routes de MovieAPI
app.include_router(movie_api.router, prefix="/movies", tags=["Movies"])

app.include_router(auth_router,prefix="/auth", tags=["Auth"])

if __name__ == "__main__":
    port = int(os.getenv("PORT",8000))
    uvicorn.run(app,host="0.0.0.0", port=port)
