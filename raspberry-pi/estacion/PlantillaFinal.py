import json
import time

# --- ENVÍO JSON (Sección 8.8.1) ---
contador_json += 1
if contador_json >= 2: # Cada 2 ciclos (aprox. 8 segundos)
    datos = {
        "temperatura": round(temperatura, 2),
        "humedad": round(humedad, 2),
        "presion": round(presion, 2),
        "luz": round(luz, 2),
        "estado_luz": estado_luz,
        "lluvia_acumulada": round(lluvia_acumulada, 4),
        "voltaje_veleta": round(voltaje_veleta, 3),
        "direccion_viento": direccion_viento,
        "velocidad_viento": round(velocidad_viento, 2),
        "intervalo_actualizacion": "1 minuto"
    }
    
    ARCHIVO_JSON = "/home/pi/PROYECTO_SCRIPTS/UNIVERSALES/datos_sensor.json"
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print("JSON generado correctamente.")
    contador_json = 0


# --- PLANTILLA METEOCLIMATIC (Sección 8.8.2) ---
CODIGO_ESTACION = "ESCAT0800000008226A"
ARCHIVO_TXT = "/home/pi/PROYECTO_SCRIPTS/UNIVERSALES/meteoclimatic.txt"
INTERVALO_TXT = 2
contador_txt += 1

def fecha_hora_meteoclimatic():
    return time.strftime("%d/%m/%Y %H:%M", time.localtime())

if contador_txt >= INTERVALO_TXT:
    contenido = (
        "*VER=DATA2\n"
        f"*COD={CODIGO_ESTACION}\n"
        f"*UPD={fecha_hora_meteoclimatic()}\n"
        f"*TMP={temperatura:.1f}\n"
        f"*WND={velocidad_viento:.1f}\n"
        f"*AZI={direccion_viento}\n"
        f"*BAR={presion:.1f}\n"
        f"*HUM={humedad:.0f}\n"
        f"*SUN={luz:.1f}\n"
        f"*DPCP={lluvia_acumulada:.1f}\n"
        "*EOT*"
    )
    with open(ARCHIVO_TXT, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print("TXT Meteoclimatic generado correctamente.")
    contador_txt = 0
