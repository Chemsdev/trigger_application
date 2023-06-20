# On utilise python comme image de base.
FROM python:3.8-slim-buster

# On renseigne le dossier principal de l'application.
WORKDIR /app

# On copie le fichier requirements.txt
COPY requirements.txt .

# On lance le pip install du fichier requirements.
RUN pip install --no-cache-dir -r requirements.txt

# On copie le fichier bdd.py
COPY bdd.py .

# On renseigne la ligne de commande pour exécuter l'app.
CMD ["python", "bdd.py"]
