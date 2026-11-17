# IMPORTACIONES
# Importamos board igual que antes con el BME280 para interpretar I2C con GPIO.
import board
# Importamos time para realizar las pausas de lectura
import time
# Importamos adafruit bh1750, librería que actuará de driver con el propio sensor.
import adafruit_bh1750

# Creamos una variable que será igual a la conexión I2C realizada sobre las Raspberry
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

while True:
    print(f"Luz: {sensor.lux}" "lux")
    time.sleep(1)
    if sensor.lux >= 1000:
        print("Te encuentras en el exterior")
    elif sensor.lux >= 100:
        print("Te encuentras en un edificio o casa")
    elif sensor.lux >= 0:
        print("ES DE NOCHE")
