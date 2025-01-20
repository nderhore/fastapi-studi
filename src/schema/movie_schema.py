from pydantic import BaseModel
from typing import Optional

# Schéma pour créer ou mettre à jour un film
class MovieCreate(BaseModel):
    title: str
    director: str
    year: int
    genre: str

# Schéma pour les réponses (inclut l'ID)
class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True