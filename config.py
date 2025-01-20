# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22660802"))
API_HASH = getenv("API_HASH", "fec849af712bc23ab5f18277b1592d2e")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6069621485").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://AniReal123:AniReal123@anireal123.wqnsp.mongodb.net/?retryWrites=true&w=majority&appName=AniReal123")
LOG_GROUP = getenv("LOG_GROUP", "-1002335115531")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "omegalinks.in")
AD_API = getenv("AD_API", "2919fa4e63a974e6708d8870c759728dcec1d315")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
