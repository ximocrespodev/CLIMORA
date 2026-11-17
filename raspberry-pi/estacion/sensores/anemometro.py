# Importaciones
# Importamos gpiozero, ya que vamos a tratar el anemómetro como un botón que va a recibir bits (pulsos por vuelta)
from gpiozero import Button
# Importamos math para poder realizar operaciones matemáticas
import math
# Importamos time para poder realizar las pausas adecuadas
import time

# Creamos una variable con el radio del anemómetro (9 cm)
radio = 9.0
intervalo_lectura = 5

# Realizamos las conversiones adecuadas para poder recibir los datos en KM/H
CM_IN_A_KM = 100000.0
SECS_IN_A_H = 3600

# Creamos una variable calibradora (número que rectifica resultados evitando margen de error)
calibracion = 1.18

# Utilizamos bounce_time para evitar "clicks electrónicos" falsos
velocidad_sensor = Button(5, bounce_time=0.01)

# Empezamos la cuenta en 0
cuenta_inicial = 0

# Creamos una función que va a representar una vuelta completa
def vuelta():
    global cuenta_inicial
    cuenta_inicial += 1
    print("Vuelta: " + str(cuenta_inicial))

# Creamos una función que nos calcule la velocidad en km/h
def velocidad_km(time_sec):
    global cuenta_inicial
    circunferencia_cm = (2 * math.pi) * radio
    # Una rotación completa equivale a 2 "clicks electrónicos"
    rotaciones = cuenta_inicial / 2
    # Calculamos la distancia y la pasamos a KM
    dist_km = (circunferencia_cm * rotaciones) / CM_IN_A_KM
    km_per_sec = dist_km / time_sec
    km_per_hora = km_per_sec * SECS_IN_A_H
    return km_per_hora * calibracion

# GPIOZERO va a estar leyendo constantemente los eventos en velocidad_sensor
velocidad_sensor.when_pressed = vuelta

# Imprimimos por terminal el resultado cada X segundos
while True:
    cuenta_inicial = 0
    time.sleep(intervalo_lectura)
    print(f"Velocidad del viento: {velocidad_km(intervalo_lectura):.2f} km/h")
