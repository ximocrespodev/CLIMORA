# IMPORTACIONES
# Importamos time para realizar las pausas adecuadas
import time
# Importamos board para poder interactuar los GPIO
import board
# Importamos busio como alternativa a los anteriores casos para poder interpretar el canal I2C
import busio
# Importamos de adafruit el ADS1115, el chip que se encargará de interpretar los resultados correctamente.
import adafruit_ads1x15.ads1115 as ADS
# Importamos analogin, importante para pasar de analogico a digital
from adafruit_ads1x15.analog_in import AnalogIn

# Inicializar I2C (declaramos la conexión con los SCL y SDA)
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializar ADS1115 (driver que utilizaremos para interpretar los resultados)
ads = ADS.ADS1115(i2c)

# Leer canal A0 (canal del sensor ADS1115, donde llegan las diferentes resistencias)
chan = AnalogIn(ads, 0)

# Creamos un diccionario con las aproximadas lecturas de las direcciones correspondientes (resistencias).
direcciones = {
    "N": 0.567,
    "NE": 1.046,
    "E": 1.497,
    "SE": 2.548,
    "S": 3.175,
    "OS": 3.076,
    "O": 2.886,
    "NO": 2.094
}

# Creamos una función para sacar la media de la 10 lecturas que se van a realizar en 50 milisegundos
def leer_media(num_muestras=10, pausa=0.05):
    total = 0.0
    for _ in range(num_muestras):
        # Cada muestra se va a sumar a la variable total
        total += chan.voltage
        time.sleep(pausa)
    # Devolvemos la media final
    return total / num_muestras

# Ahora vamos a crear una función que identifique a qué dirección del diccionario se acerca más la media obtenida
def obtener_direccion(voltaje):
    # Se aplica la función min y lambda para restar el valor del diccionario con el voltaje obtenido
    direccion_cercana = min(direcciones, key=lambda d: abs(direcciones[d] - voltaje))
    return direccion_cercana

# Creamos un bucle para leer las resistencias constantemente cada segundo
while True:
    voltaje = leer_media()
    direccion = obtener_direccion(voltaje)
    # Aplicamos :.3f para indicar que solo queremos 3 décimas detrás del número principal
    print(f"Resistencia media: {voltaje:.3f} V")
    print(f"Dirección del viento: {direccion}")
    print("-" * 30)
    time.sleep(1)
