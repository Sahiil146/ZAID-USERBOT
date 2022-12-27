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
STRING_SESSION3 = getenv("STRING_SESSION3", "BQB_KYZH1_XXjFxxbgEJil3q2JEOB74FFhmV0gEfC-Zs0gV9jo59Cu6lydpiws1XzNzDo5ktgQvFfM8XiD4rAwEz1cbs_uls_MteY8lXtWy_ryG4Ix2kjk08dHExC8Es_ukSoWSa6KbvT9tStP0lZUMgn4ghYAdI8-aqXhPEk8Ik3UXWih4nDARCFk6WTykXOCPjHySufJh1sVhmBUajtz-BjgVg7cUjext0ZThGLMwztkYZ7rBXmpU6VtMrL0ESEJkMAJ-qjFozCNZqwkOljUrj8MxjZbMFxy_S1pTSXVso3b0809ss9E6GB1go4_BS3m60PVKWx6mqNuEUOLnybyTHAAAAASw4Z88A")
STRING_SESSION4 = getenv("STRING_SESSION4", "BQA740JUvHuYLxQseJOv9QIzBIJUiso-Tw8aUqNYQ3o_JL1X9zafg97MMb4m9p5HNVOUUAY1Dv2562K1vlS7sXBQeg56YbZqD1vA50i9nFp3KeJqcne9-4fHkb1NaHUvO7aw1ojRnB116PFsBzR6SUZjRaUFeEdoXsMSzimRDSzDTVQ4vC3NgMQ_97UtC_k-5yS9_Ha1wyGJz-o-0U1gqM2CC8SZVIFUbIqH15uj_s_1UEN3bfxQiOW_AWxaRzNThnfg_8uZTssLqMbRks9KP8igdF4bqwQrTtV0AQCOgQLxJjpnf6iI_i60li0pdBlvpuIGYdtKEvHo04B8kX1OgddxAAAAAWRTxGYA")
STRING_SESSION5 = getenv("STRING_SESSION5", "AQB3dn1e2NcBFZSFLf-4XdqFxXIY1fr8ArSYXYZpiBoM91-uKdqvZJrrivYiLQY9YEK7l26_q9pLY463uqsTnc9rwnZYbObyWJquIwv61hbwT_q4xqu7jqJx_Vvmzgf_frwzn0iJrVJagig-q6GOrFSSkgUoByhY5Z6kt-9GE-zoqIBZlXYJmXMJ8eyisaOMzixAFJlTHofDIse1giiCrujXwlXio7NncnrjAKCILeb_31hPQRpgIzenOJxwh5cWzJVz_bgT4R4o0Mw112b7f2NbMrkKOfwH-g6BuX2Hz3M3oIYJzDHaLXetJtOkIYFYvuomVNh77OzvOUZ_j9bJk-ENAAAAAWP_oOsA")
STRING_SESSION6 = getenv("STRING_SESSION6", "AQC6i8_DQLgn-2rxTkzPYWg5DFxAMgnzrJmotqxNi932YxHkOqdEqbmt-Ze84NC01LrYYPoOsC8Xy2yjzwSrG6yyqdZ27uzcSo3-460hjw1FbdDvi6R9c2kgREL3chmYdANF8mH1-ucJGN00Na0ZmMLYlSdWVJ_vgfUCf-1teTghKpOSmJ3Fg1f5JAg_U4s_Gt4N3kMbRJR3oK8iRamhuYqNZLByvjju2h88GdJItaoi5uxEimiL6TPwXkymNQIppdbFnWrCi4KFTR3nE97qSesGPvZsnA1K3Aix7O6LzFeYb5dMbSGI63qDFjAdkc6XEhWqn0RZpXw_VKpybOvlTLqoAAAAAVqyhcAA")
STRING_SESSION7 = getenv("STRING_SESSION7", "AQAY1x_v-Er-mAviOFVkLvpuerjNtUtwfEIwaem-9OVQj_QfKKve5TLFawvKHYCRgkfWNc8Ruy-6vpqBk9xtiEL6Ag0GJW-djRpoeTtY4glhlrIUAu2Ak9X-YufYvEVxjTR608GqGgb9gCl2n_F7a0mCcdtzW28zpxD0HWK1ndhulWhO8zcQWba3GL9sxCvaMPLdQqowh3JtD_DpNd8QJfCnoWm-r8-ZJa3mQcokswfZNL4c8k0TBvfezAjIV8lwXzY-1wob8AjCW435Qw_Ayu16L_85071fc-kDwDBrjkm4gWupgpqCzAfdP3jVNH5_9NAIWOqKBX30WogIipCPu8OQAAAAAWE8TUsA")
STRING_SESSION8 = getenv("STRING_SESSION8", "AQAN0RHSpB6lAczaUJDfUCM6EgJl6rMrS_GRJnT2M8vXQhDYYhcYa-9PVoKPZyyI2TYi3GtzllnbJRW4ADDPrKJyM3dmC6_fUaTKP4rHuDBUDAMOq2S57436mV6GUz1YaPEIMQmTiWTHo9V1KD7x9u36fXICpofyOfFKkkJKGfE9Qkf4B-x_0Svso8XuWN7jT2RIKuCnfoEVAzqzeofXubPB-C3yCcuuqb2FFF1X4p4XETE8GG0vbKknrwtyK_paVRFox0cbI4PPRwq4RseBhL0n-rstCQNURnn9Z2Ry0ztWZLMHkjcuOI-wecVmksCzUx5idfMCf5n4OGvXy2SMjtp6AAAAAWPicWUA")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
