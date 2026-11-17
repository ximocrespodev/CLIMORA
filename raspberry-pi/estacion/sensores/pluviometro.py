# IMPORTACIONES
# Importamos button de gpiozero ya que vamos a tratar el pluviómetro como un interruptor que cierra y se abre.
from gpiozero import Button
# Importamos time para poder realizar las pausas adecuadas
import time

# Identificamos al sensor en el GPIO 6 de nuestra raspberrypi
rain_sensor = Button(6, bounce_time=0.05) # bounce_time recomendado para evitar rebotes electrónicos en gpiozero

# Creamos una variable que identifica la cantidad de agua que cabe en mm en el pluviómetro.
BUCKET_SIZE = 0.2794
count = 0

# Creamos una función que se llamará cuando se reciban bits positivos (o cuando el botón esté pulsado, aplicando esta lógica).
def bucket_lleno():
    global count
    count += 1

# gpiozero siempre va a estar comprobando todos sus eventos con un bucle infinito interno. Por lo que igualamos la acción del botón pulsado a la anterior función.
rain_sensor.when_pressed = bucket_lleno()

# Bucle principal: imprimir cada X segundos
intervalo_impresion = 5 # segundos

# Creamos un bucle para recibir resultados por terminal
while True:
    lluvia_acumulada = count * BUCKET_SIZE
    print(f"Lluvia acumulada: {lluvia_acumulada:.4f}")
    time.sleep(intervalo_impresion)
