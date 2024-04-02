from telegram.ext imp ort Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Hi! Send me a YouTube link or a search query and I will play the audio or video in the voice chat.')

def echo(update, context):
    update.message.reply_text('Sorry, I only accept YouTube links or search queries for now.')

def play_media(update, context):
    query = update.message.text
    if query.startswith('http'):
        video_url = query
    else:
        # Your code to search for and get the video URL
        pass

    # Your code to download and send the video or audio
    pass

def main():
    updater = Updater("7167523778:AAGIWs5N5ko8gNVIV8cgs1Trq9Wp57PL7wk", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(MessageHandler(Filters.text & Filters.regex(r'^http(s)?://'), play_media))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, play_media))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
