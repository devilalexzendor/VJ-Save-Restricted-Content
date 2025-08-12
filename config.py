import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8251653078:AAFFPpR8oFvSZJZVWf3WfWmFvdQ58W7gcNQ")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20708013"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f0dbe59c7e43cc49fe9e83206ef9f828")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1188631841"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
