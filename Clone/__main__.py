from pyrogram import Client



# Set up bot configurations
API_ID = 29764570
API_HASH = "7676192e491329a1b859b2184e5d7823"
TOKEN = "7402282033:AAFnpVWwM3kCW1_HtZqRdGspatFl6_ZbLgE"

#PYROGRAM BOT CLIENT
bot = Client(name="CloneBot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Clone.Examples"))
      
if __name__ == "__main__":
      bot.run()
