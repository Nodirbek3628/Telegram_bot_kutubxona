from telegram import Update
from telegram.ext import CallbackContext


def start(update:Update,context:CallbackContext):
    user = update.message.from_user.full_name
    update.message.reply_text(
        f"Assalomu Alaykum.Botimizga xush kelibsz xurmatli {user}"
    )


def helpi(update:Update,context:CallbackContext):
    update.message.reply_text("Qanday yordam bera olaman ")

def stop(uptade:Update,context:CallbackContext):
    user = uptade.message.from_user.full_name
    uptade.message.reply_text(
        f"Tashrifinggiz uchun tashakkur {user}"
    )

def echo(update:Update,context:CallbackContext):
    update.message.reply_text(update.message.text)

def contact(update:Update,context:CallbackContext):

    phone = update.message.contact.phone_number
    name = update.message.contact.first_name
    contact = update.message.contact
    update.message.reply_contact(
        f"Raqaming {phone} ismingiz {name}"
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

def audio(update:Update,context:CallbackContext):
    audio = update.message.audio
    update.message.reply_audio(audio=audio)

def sticker(update:Update,context:CallbackContext):
    sticker = update.message.sticker
    update.message.reply_sticker(sticker=sticker)

def location(update:Update,contect:CallbackContext):
    location = update.message.location
    update.message.reply_location(location=location)