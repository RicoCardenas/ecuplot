from pyrogram.types import InlineKeyboardButton

class DecoradoresPerfil:
    def __init__(self):
        self.botones = [
                [
                    InlineKeyboardButton(text='Instrucciones', callback_data='instrucciones'),
                    InlineKeyboardButton(text='Acerca', callback_data='acerca')
                ],
                [
                    InlineKeyboardButton(text='Atras', callback_data='back')
                ]
        ]

        self.perfil_mensaje = f"""
𝙀𝙘𝙪𝙥𝙡𝙤𝙩                © 2024

Gracias por usar EcuPlot.
"""