from pyrogram.types import InlineKeyboardButton

class DecoradoresStart:
    def __init__(self):
        self.botones = [
                [
                    InlineKeyboardButton(text='Instrucciones', callback_data='instrucciones'),
                    InlineKeyboardButton(text='Acerca de mi', callback_data='acerca')
                ],
                [
                    InlineKeyboardButton(text='Perfil', callback_data='perfil')
                ]
        ]

    def mensajeStart(self, user_name):
        return f"""
Bienvenido **{user_name}!**, Soy **Ecuplot**.

Soy un bot con el que puedes graficar funciones.
Aqui podras encontrar las herramientas con las que cuento!
"""