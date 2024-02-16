# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "1779071")

API_HASH = os.environ.get("API_HASH", "3448177952613312689f44b9d909b5d3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5001274197:AAGqyMO0PnFKP13SYGtkXokjkL_zsyvwypo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "TamilBots") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "filestream")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://filestream:filestream@cluster0.d1dlfzv.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e84aa7ea3d03578317a87.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1169076058').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
