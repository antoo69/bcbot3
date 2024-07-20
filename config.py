import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7254722365:AAEkvVBHV1kE-yKyj3RIGlzXdYN9C4-_H-c")
API_ID = int(os.environ.get("API_ID", "29305295"))
API_HASH = os.environ.get("API_HASH", "6838cc67172f18fe5f302c158ce2fbfa")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002079962899"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "2012224978").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://kcici715:buburayam1@cluster0.clpcyju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "kcici715")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
