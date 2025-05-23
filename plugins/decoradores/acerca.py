from pyrogram.types import InlineKeyboardButton

class DecoradoresAcerca:
    def __init__(self):
        self.botones = [
                [
                    InlineKeyboardButton(text='Instrucciones', callback_data='instrucciones'),
                    InlineKeyboardButton(text='Perfil', callback_data='perfil')
                ],
                [
                    InlineKeyboardButton(text='Atras', callback_data='back')
                ]
        ]

        self.acerca_mensaje = f"""
𝙀𝙘𝙪𝙥𝙡𝙤𝙩                © 2024

ʙʏ:
Julian Cardenas
Mateo Ibarra
"""