from pyrogram.types import InlineKeyboardButton

class DecoradoresInstrucciones:
    def __init__(self):
        self.botones = [
                [
                    InlineKeyboardButton(text='Acerca', callback_data='acerca'),
                    InlineKeyboardButton(text='Perfil', callback_data='perfil')
                ],
                [
                    InlineKeyboardButton(text='Atras', callback_data='back')
                ]
        ]

        self.instrucciones_mensaje = f"""
𝙀𝙘𝙪𝙥𝙡𝙤𝙩                © 2024

Como escribir las Funciones
Antes de enviar una funcion
usar comando **/graficar**
Para ecuacion lineal
/graficar 4x
Para ecuacion cuadratica
/graficar 4x^2 + x + 2
Para ecuacion cubica
/graficar 4x^3 + x
Para ecuacion racional
/graficar 4x/3
Para ecuaciones de raices
/graficar sqrt(x)

Para agregar mas de una grafica utilizar simbolo Ampersand (&)
Ejemplo: /graficar x & sqrt(x)
"""