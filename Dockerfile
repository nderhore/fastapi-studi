# 1. récuperation de l'image Python en version 3.13.1
FROM python:3.13.1-alpine3.21

# 2. Je vais créer mon systeme de fichier dans mon container
# mkdir /app && cd
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installation des dependances
RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python", "main.py"]