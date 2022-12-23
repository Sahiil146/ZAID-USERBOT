import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "22939641")) #optional
API_HASH = getenv("API_HASH", "8854a48ffd429bd794e070a4d1c12be7") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5036861391").split()))
OWNER_ID = int(getenv("OWNER_ID", "5659722901"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Suraj:sahil11@sahiil11.rqe6gne.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5951338086:AAGHs98bCCWauKr9bYFp7mPMIK2qsmdImzs")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQClfuQZ3m_32EcIvreHJY9egUP-JxlidhNePQdNpuThBjZQ-wbiQiTnPwOBnZptf_yfVzvHrhjhxNQvsYJZlWAqenTNqsNCelbpVPPlq4fBxIggSduL5GUCC6K4jheYL1nl42KnHSc1fN115xePmUBtch0cwwcOtgSAZ7w14p2wZRhQN2r6A1uTRy_46ZRcHQoWsN-pPB_wU3R4s3y1BKjepiVYu3WqkfXVhmcwdylC1V5IWrl_ngq-AQOMBIdE8pqTdL6mLKfM6bzFf-0DhA2ka12odVIV4Kz8A22jCHKsK7GXu2YIRhKJ6eGcdzaUEl3PVYkHdR5z4_GayDhHgma6AAAAAVG25UEA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQBO8IwxuBPhoLqNM8Earh-4oZEYoPJ6FhLS7FDZbLHPVwebblELuImeaicMUEO_4tPweIP-jutBWxKm2juXGDXp8U9RcHk80aEcE2n5unjNi9roZr2PiTbdMMtL8ZoavoQr6Rt6k2uDhjQhjXg22lXgbzmjSGSViqjg28M9TDFM7bUHb6p6U6bgIgiNXhgNUKHLtZsW-kBRuJCrkKDMlvQEhzRjvv2cfmZK_CT9CSr1vVNNjNvqiYOrWt0-5POftUCar06_J-otIGvT_DQ_Qm9oUBItivlVwQYKDpmL0xdJqxHUrSLGpBF8SrgZ4czr4PV2iM4yUiIxv75P9YRZ2zhQAAAAAV5uOZsA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
