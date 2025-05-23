import io
from matplotlib import pyplot

class DibujarFuncion:
    def __init__(self):
        self.image_bytes = None

    # Función cuadrática.
    def dibujar_funcion_1(self, x):
        print(x)
        print(x**4 + 5)
        return (x ** 4) + 5

    # Función lineal.
    def dibujar_funcion_2(self, x):
        return 4 * x + 1

    def dibujar_grafica(self):
        buf = io.BytesIO()
        # Valores del eje X que toma el gráfico.

        x = range(-10, 15)
        # Graficar ambas funciones.
        pyplot.plot(x, [self.dibujar_funcion_1(i) for i in x])
        pyplot.plot(x, [self.dibujar_funcion_2(i) for i in x])
        # Establecer el color de los ejes.
        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")
        # Limitar los valores de los ejes.
        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)
        # Guardar gráfico como imágen PNG.
        pyplot.savefig(buf, format='png')
        buf.seek(0)

        self.image_bytes = buf.read()
        # Mostrarlo.
        pyplot.show()