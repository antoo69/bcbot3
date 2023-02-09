import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6054586380:AAGh0oYvdxUU1cI13JHcj_UG4RIZq4AOJZs")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001746351071"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "2012224978").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://rexa:rexa@rexa.lyguuwj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "rexa")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
