# IMPORTACIONES
# Para poder utilizar time.sleep y poder realizar pausas entre las lecturas
import time
# Importamos board para poder aplicar el estándar utilizado de I2C junto los pines de GPIO
import board
# Importamos basic de la librería adafruit_bme280, esta librería va a actuar como un driver para que la raspberry pueda interpretar los resultados correctamente.
from adafruit_bme280 import basic as adafruit_bme280

# Creamos una variable que equivaldrá a la conexión que realizaremos por i2c
i2c = board.I2C()

# Creamos una variable, la cual utiliza un método especial de la librería basic que hemos declarado al principio, este método se conoce como Adafruit_BME280_I2C y crea el propio objeto de BME280. A este método, le tenemos que pasar la conexión I2C y la dirección física del sensor.
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Ahora simplemente, crearemos un bucle while donde aplicaremos los métodos que nos ofrece adafruit con la variable que hemos creado anteriormente (bme280).
while True: # Bucle infinito para ir actualizando los datos
    print(f"Temperatura: {bme280.temperature:.2f} °C")
    print(f"Humedad: {bme280.humidity:.2f} %")
    print(f"Presión: {bme280.pressure:.2f} hPa")
    print("-" * 30)
    time.sleep(2) # Indicamos un tiempo de espera de 2 segundos hasta la siguiente lectura.
