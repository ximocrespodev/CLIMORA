# IMPORTACIONES
# Importamos board para comunicarnos correctamente con los GPIO siguiendo I2C.
import board
# Importamos adafruit_ssd1306 como driver con nuestra pantalla OLED.
import adafruit_ssd1306
# Importamos dependencias de PIL para trabajar con la pantalla (imagen, dibujo, fuentes):
from PIL import Image, ImageDraw, ImageFont

# 1) Tamaño de la pantalla OLED
ANCHO = 128
ALTO = 64

# 2) Crear la conexión I2C
i2c = board.I2C()

# 3) Crear el objeto de la pantalla OLED
oled = adafruit_ssd1306.SSD1306_I2C(ANCHO, ALTO, i2c)

# 4) Limpiar la pantalla
oled.fill(0)
oled.show()

# 5) Crear una imagen en blanco y negro
imagen = Image.new("1", (ANCHO, ALTO))
dibujo = ImageDraw.Draw(imagen)

# 6) Cargar una fuente básica
fuente = ImageFont.load_default()

# 7) Escribir texto en la imagen
dibujo.text((40, 25), "Climora", font=fuente, fill=255)

# 8) Enviar la imagen a la pantalla OLED
oled.image(imagen)
oled.show()
