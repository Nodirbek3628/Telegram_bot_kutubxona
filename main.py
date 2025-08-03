from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from config import TOKEN
from handlers import start,helpi,echo,contact,photo,vedio,voice,audio,sticker,stop,location

  


def main()->None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    #CommandHandler
    dispatcher.add_handler(CommandHandler("start",start))
    dispatcher.add_handler(CommandHandler("help",helpi))
    dispatcher.add_handler(CommandHandler("stop",stop))
    

    #MessageHandler
    dispatcher.add_handler(MessageHandler(Filters.text,echo))
    dispatcher.add_handler(MessageHandler(Filters.contact,contact))
    dispatcher.add_handler(MessageHandler(Filters.photo,photo))
    dispatcher.add_handler(MessageHandler(Filters.video,vedio))
    dispatcher.add_handler(MessageHandler(Filters.voice,voice))
    dispatcher.add_handler(MessageHandler(Filters.audio,audio))
    dispatcher.add_handler(MessageHandler(Filters.sticker,sticker))
    dispatcher.add_handler(MessageHandler(Filters.location,location))


    updater.start_polling()     # While tru vazifasini bajaradi
    updater.idle()              # While   
    
main()