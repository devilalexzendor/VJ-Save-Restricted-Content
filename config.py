import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8326718294:AAEK-f15fLLz04OJltjKsm9mJeA495aYRpo")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22370423"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "026eada47b6991f2a9eec8461c7febb5")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8150558323"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
