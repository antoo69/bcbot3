import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7334901884:AAESRz4TEgqGZqbzkC_ErBeZJUj1ta4VhkI")
API_ID = int(os.environ.get("API_ID", "28518520"))
API_HASH = os.environ.get("API_HASH", "c858cde56cb2b2050a64df7e65de567b")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002236001760"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6681099028").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://kcici715:buburayam1@cluster0.clpcyju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "kcici715")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
