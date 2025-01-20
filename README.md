# API de Gestion de Films avec FastAPI

## Fonctionnalités

- Ajouter de nouveaux films avec des détails comme le titre, le réalisateur, l'année de sortie et le genre.
- Récupérer tous les films ou un film spécifique par ID.
- Mettre à jour les détails d’un film.
- Supprimer un film.
- Documentation interactive de l'API auto-générée avec Swagger UI.

---

## Instructions d'Installation

### Prérequis

- Python 3.8+
- pip (installé avec Python)

### Étapes d'Installation

1. **Cloner le Dépôt**

   ```bash
   git clone https://github.com/nderhore/fastapi-studi.git
   cd fastapi-studi
   ```

2. **Créer un Environnement Virtuel**

   ```bash
   python -m venv env
   source env/bin/activate  # Sous Windows : env\Scripts\activate
   ```

3. **Installer les Dépendances**

   ```bash
   pip install -r ./requirements.txt
   ```

4. **Lancer l'Application**

   ```bash
   python -m uvicorn main:app --reload
   ```

5. **Accéder à l'API**

   - Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/docs` pour Swagger UI.

---

## Points d'Entrée de l'API

### URL de Base

`http://127.0.0.1:8000/movies`

### Endpoints

1. **Créer un Film**
   - **POST** `/`
   - Corps de la Requête :
     ```json
     {
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genre": "Science Fiction"
     }
     ```
   - Réponse :
     ```json
     {
       "id": 1,
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genre": "Science Fiction"
     }
     ```

2. **Récupérer Tous les Films**
   - **GET** `/`
   - Réponse :
     ```json
     [
       {
         "id": 1,
         "title": "Inception",
         "director": "Christopher Nolan",
         "year": 2010,
         "genre": "Science Fiction"
       }
     ]
     ```

3. **Récupérer un Film par ID**
   - **GET** `/{movie_id}`
   - Réponse :
     ```json
     {
       "id": 1,
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genre": "Science Fiction"
     }
     ```

4. **Mettre à Jour un Film**
   - **PUT** `/{movie_id}`
   - Corps de la Requête :
     ```json
     {
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genre": "Thriller"
     }
     ```
   - Réponse :
     ```json
     {
       "id": 1,
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genre": "Thriller"
     }
     ```

5. **Supprimer un Film**
   - **DELETE** `/{movie_id}`
   - Réponse :
     ```json
     {
       "id": 1,
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genre": "Science Fiction"
     }
     ```

---


