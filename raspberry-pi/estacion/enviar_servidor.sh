#!/bin/bash
while true
do
    scp /home/pi/PROYECTO_SCRIPTS/UNIVERSALES/datos_sensor.json administrador@benissa.3utilities.com:/var/www/climora.es/wp-content/datos
    scp /home/pi/PROYECTO_SCRIPTS/UNIVERSALES/meteoclimatic.txt administrador@benissa.3utilities.com:/var/www/climora.es/wp-content/datos
    sleep 10
done
```[cite: 82]

---

<ElicitationsGroup message="¿Quieres que pasemos a los scripts de configuración del Servidor Marta (Apache VirtualHosts, ProFTPD) o prefieres otra sección?">
  <Elicitation label="Configuración del Servidor (Apache y FTP)" query="Pasemos a la carpeta de configuración del servidor con Apache y ProFTPD."/>
  <Elicitation label="Otro apartado del documento" query="Prefiero revisar otra parte del documento PDF de Climora."/>
</ElicitationsGroup>
