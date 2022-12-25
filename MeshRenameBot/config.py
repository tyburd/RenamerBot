from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "postgres://hcslrwpy:QQiW_-rDRONHeIFKVVx19cJf6zdt1GsR@heffalump.db.elephantsql.com/hcslrwpy"]
        API_HASH = [str, "ab24cb10939b6505b23891e21df11d1f"]
        API_ID = [int, 14691136]
        BOT_TOKEN = [str, "5832854330:AAHFWJwS9VC1vQQdNuLLm_YRSPkPf-exbOY"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 10]
        SLEEP_SECS = [int, 15]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID = [int, 123456789]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,-100123465978]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
        BROADCAST = "/broadcast"
        STATS = "/stats"
