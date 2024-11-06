# Utiliser une image de base Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY app /app
COPY frontend /frontend

# Exposer le port Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["flask", "run", "--host=0.0.0.0"]

