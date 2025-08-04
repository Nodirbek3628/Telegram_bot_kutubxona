from telegram import Update
from telegram.ext import CallbackContext


def start(update:Update,context:CallbackContext):
    user = update.message.from_user.full_name
    update.message.reply_text(
        "🇺🇿 *Assalomu alaykum!*\n"
        "🤖 Siz *Valyuta Konvertatsiya* botiga xush kelibsiz!\n\n"
        "💱 Ushbu bot orqali siz istalgan valyutani boshqa valyutaga avtomatik hisoblab olishingiz mumkin.\n\n"
        "📌 *Foydalanish tartibi:*\n"
        "👉 Faqat quyidagi formatda yozing: `USD-UZS-100`\n"
        "   (ya'ni: qaysi valyutadan - qaysi valyutaga - miqdori)\n\n"
        "✅ *Misollar:*\n"
        "   🔹 `USD-UZS-100` → 100 AQSH dollari necha so'm?\n"
        "   🔹 `UZS-USD-500000` → 500,000 so'm necha dollar?\n"
        "   🔹 `EUR-RUB-50` → 50 yevro necha rubl?\n"
        "   🔹 `GBP-USD-30` → 30 funt sterling necha dollar?\n"
        "   🔹 `JPY-USD-10000` → 10,000 yapon iyenasi necha dollar?\n"
        "   🔹 `AZN-UZS-25` → 25 ozarbayjon manati necha so'm?\n"
        "   🔹 `BRL-USD-100` → 100 braziliya reali necha dollar?\n"
        "   🔹 `AFN-USD-1000` → 1,000 afg'on afg'anisi necha dollar?\n\n"
        "🌐 Valyuta kodlari ISO 4217 standartida bo'lishi kerak (masalan: USD, EUR, GBP, RUB, UZS, KZT, CAD, JPY, va boshqalar).\n\n"
        "🕐 Kurslar O'zbekiston Markaziy Banki yoki boshqa ochiq API manbalaridan olinadi.\n\nYordam kerak bo'lsa /help tugmasini bosing"
        
    )


def helpi(update:Update,context:CallbackContext):
    update.message.reply_text(
        "ℹ️ Yordam: `USD` - AQSH dollari, `EUR` - Yevro, `UZS` - So'm,\n"
        "`RUB` - Rubl, `GBP` - Funt sterling, `JPY` - Yapon iyenasi,\n"
        "`AZN` - Ozarbayjon manati, `BRL` - Braziliya reali, `AFN` - Afg'on afg'anisi."
        
    )

def stop(uptade:Update,context:CallbackContext):
    user = uptade.message.from_user.full_name
    uptade.message.reply_text(
        f"Tashrifinggiz uchun tashakkur {user}"
    )

def echo(update:Update,context:CallbackContext):
    update.message.reply_text(update.message.text)

def contact(update:Update,context:CallbackContext):
    contact = update.message.contact
    update.message.reply_contact(
        first_name = contact.first_name,
        phone_number = contact.phone_number
    )

def photo(update:Update,context:CallbackContext):
    photo = update.message.photo[-1].file_id
    update.message.reply_photo(photo)

def vedio(update:Update,context:CallbackContext):
    vedio = update.message.video
    update.message.reply_video(vedio)

def voice(update:Update,context:CallbackContext):
    voice = update.message.voice
    update.message.reply_voice(voice=voice) 
    update.message.reply_voice("Ovoz yuborng")

def audio(update:Update,context:CallbackContext):
    audio = update.message.audio
    update.message.reply_audio(audio=audio)

def dice(update:Update,context:CallbackContext):
    dice = update.message.dice
    update.message.reply_dice(
        emoji = dice.emoji
    )

def sticker(update:Update,context:CallbackContext):
    sticker = update.message.sticker
    update.message.reply_sticker(sticker=sticker)

def location(update:Update,contect:CallbackContext):
    location = update.message.location
    update.message.reply_location(location=location)