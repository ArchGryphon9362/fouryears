#from flask import Flask
import requests
import os
import telebot

#app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
FOUR_TOKEN = os.environ.get("FOUR_TOKEN")
GIB2KIB = 1024 * 1024

#@app.route("/")
def main():
	headers = {
		"Accept": "application/json",
		"x-gg-auth": FOUR_TOKEN
	}
	fouryears = requests.get("https://48.ie/panda/protected/users/339696/sims/893531118020807745/balance/summary/current", headers=headers).json()
	remaining_roam = int(fouryears["_payload"]["current_month_balance_summary"]["left_fup_data"])
	gib = remaining_roam / GIB2KIB
	mb = round((gib * 1000) % 1000)
	kb = round((gib * 1000 * 1000) % 1000)
	gib = round(gib)
	return f"{gib}GiB {mb}MB {kb}KB"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "data"])
def handbot(message):
	bot.reply_to(message, main())

bot.infinity_polling()
