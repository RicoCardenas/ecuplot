from pyrogram import Client, filters
from ..decoradores.instrucciones import DecoradoresInstrucciones
from ..decoradores.acerca import DecoradoresAcerca
from ..decoradores.back import DecoradoresBackButton
from ..decoradores.start import DecoradoresStart
from ..decoradores.perfil import DecoradoresPerfil
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery

@Client.on_message(filters.command(['start'], ['!','.','/']))
async def startComando(client, message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    decorador = DecoradoresStart()

    mensaje = decorador.mensajeStart(user_name)
    reply_markup = InlineKeyboardMarkup(decorador.botones)

    return await message.reply_text(mensaje, reply_to_message_id=message.id, reply_markup=reply_markup)

@Client.on_callback_query()
async def callbackBotones(_, callback:CallbackQuery):
    match callback.data:
        case 'instrucciones':
            decorador = DecoradoresInstrucciones()
            reply_markup = InlineKeyboardMarkup(decorador.botones)
            return await callback.edit_message_text(decorador.instrucciones_mensaje, reply_markup=reply_markup)
        case 'acerca':
            decorador = DecoradoresAcerca()
            reply_markup = InlineKeyboardMarkup(decorador.botones)
            return await callback.edit_message_text(decorador.acerca_mensaje, reply_markup=reply_markup)
        case 'perfil':
            decorador = DecoradoresPerfil()
            reply_markup = InlineKeyboardMarkup(decorador.botones)
            return await callback.edit_message_text(decorador.perfil_mensaje, reply_markup=reply_markup)
        case 'back':
            decorador = DecoradoresBackButton()
            reply_markup = InlineKeyboardMarkup(decorador.botones)
            return await callback.edit_message_text(decorador.back_mensaje, reply_markup=reply_markup)