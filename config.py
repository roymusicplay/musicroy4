from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBorcx_--uV89FY1mxJW_UO5DcJxn9WIVZ3tV44UjHWoquLa3t-x7ewT7XlBBP_ZCoK47-6IwZ5QMDkvt1spOl_1TFR2VxgFrjslZz8iRk007RU09Lc_v-MhlB9omZDJiCAnxhzz4EBg3H5_Eb5D9JJWjLRcPQ_CN7nhmFsAPn-AJfY6vDMirKz3pUq4HHjOm6DDUrXVW_PTf4fwlSD_XFVVEIPur90GPgA0VqBI3Dgbrt3cd2BvkHvpHrHsw55Sh4t3uEuZ9A9ibQEUU1LfZejYPs7zsrxeaIhfLS9W37cW73k7LMpFA0yo4_QKTikgfss5Dofcb2UvjyuwhBuUJZ0b5MHgAA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
