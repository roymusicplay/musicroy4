from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBorcx_--uV89FY1mxJW_UO5DcJxn9WIVZ3tV44UjHWoquLa3t-x7ewT7XlBBP_ZCoK47-6IwZ5QMDkvt1spOl_1TFR2VxgFrjslZz8iRk007RU09Lc_v-MhlB9omZDJiCAnxhzz4EBg3H5_Eb5D9JJWjLRcPQ_CN7nhmFsAPn-AJfY6vDMirKz3pUq4HHjOm6DDUrXVW_PTf4fwlSD_XFVVEIPur90GPgA0VqBI3Dgbrt3cd2BvkHvpHrHsw55Sh4t3uEuZ9A9ibQEUU1LfZejYPs7zsrxeaIhfLS9W37cW73k7LMpFA0yo4_QKTikgfss5Dofcb2UvjyuwhBuUJZ0b5MHgAA")
BOT_TOKEN = getenv("1807956602:AAH9qrMyyf2mo3kJh2jeodvDhoJkwsw_pUM")
BOT_NAME = getenv("⭐ KINGBOT MUSIC BOT⭐")
admins = {}
API_ID = int(getenv("4810374"))
API_HASH = getenv("6aafb0eab6a7f0fdedc79df7a17efb98")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
