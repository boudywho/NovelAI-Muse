import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder
import random
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your Telegram Bot Token
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Your complete list of unique artists
all_artists = [
    "ciloranko", "ask_(askzy)", "dino_(dinoartforame)", "novelace", "bigrbear", 
    "wlop", "reoen", "alphonse_(white_datura)", "as109", "relax_(artist)", 
    "miv4t", "tianliang duohe fangdongye", "tab_head", "da_mao_banlangen", 
    "mika_pikazo", "suyamori", "teranekosu", "gin00", "konya_karasue", "Been", 
    "fukuro_daizi", "kz_oji", "void_0", "ke-ta", "mignon", "rhasta", 
    "kaede_(sayappa)", "kabedoru", "asakuraf", "komota_(kanyou_shoujo)", 
    "healthyman", "modare", "shion_(mirudakemann)", "m_alexa", "mochizuki_kei", 
    "eufoniuz", "sy4", "asou_(asabu202)", "sho_(sho_lwlw)", "naga_u", 
    "henreader", "ama_mitsuki", "mikozin", "goldowl", "nekojira", "ningen_mame", 
    "qiandaiyiyu", "ohisashiburi", "liduke", "uechin_ewokaku", "bigxixi"
]

async def start(update: telegram.Update, context: CallbackContext):
    await update.message.reply_text('Hello! Use /artist to get a random list of artists.')

async def get_artist(update: telegram.Update, context: CallbackContext):
    # Generate a random number of artists between 4 and 10
    num_artists = random.randint(4, 10)

    # Select a random sample of artists
    selected_artists = random.sample(all_artists, num_artists)

    # Format the output with random brackets and multiple bracket chances
    artist_string = ""
    for artist in selected_artists:
        bracket_type = random.choice(['{', '['])  # Choose bracket type
        num_brackets = 1
        if random.random() < 0.3:  # 30% chance of 2 brackets
            num_brackets = 2
        if random.random() < 0.15: # 15% chance of 3 brackets
            num_brackets = 3
        
        # Determine the closing bracket based on the opening bracket
        closing_bracket = '}' if bracket_type == '{' else ']' 

        artist_string += f"{bracket_type * num_brackets}{artist}{closing_bracket * num_brackets}, "

    # Add the constant text
    artist_string += "year_2023, best quality, amazing quality, very aesthetic, absurdres"

    await update.message.reply_text(artist_string)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("artist", get_artist))

    application.run_polling()

if __name__ == '__main__':
    main()
