# Utiliser l'image officielle Python 3.8
FROM python:slim-bullseye
LABEL  version=v1.0.0
LABEL app=shane-app

ENV FLASK_APP=app.py
ENV FLASK_ENV=dev

WORKDIR /home/shaney/Bureau/_IBM_PREDICT_DockeerTime_/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "app.py", "--host=0.0.0.0"]
