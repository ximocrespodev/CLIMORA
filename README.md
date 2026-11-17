# ☁️ CLIMORA: Estación Meteorológica IoT & Servidor de Alta Disponibilidad
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-orange?style=for-the-badge&logo=git&logoColor=white)
<div align="center">

![Grado Medio SMR](https://img.shields.io/badge/Grado_Medio-SMR-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-4_Model_B-C51A4A?style=for-the-badge&logo=raspberry-pi)
![Apache](https://img.shields.io/badge/Apache-Server-D22128?style=for-the-badge&logo=apache)
![WordPress](https://img.shields.io/badge/WordPress-CMS-1175B8?style=for-the-badge&logo=wordpress)
![Cloudflare](https://img.shields.io/badge/Cloudflare-Security-F38020?style=for-the-badge&logo=cloudflare)

*“Tu estación, tu clima, sin sorpresas. Más cerca del cielo”*[cite: 29]

</div>

---

## 📖 Sobre el Proyecto
**Climora** nace como Proyecto Final de Grado Medio en **Sistemas Microinformáticos y Redes (SMR)**[cite: 1]. Su objetivo principal es resolver la imprecisión de las grandes aplicaciones meteorológicas comerciales mediante el despliegue de estaciones locales de alta precisión orientadas tanto al sector agrícola (prevención de riegos y pérdidas) como al ámbito público[cite: 6].

El proyecto abarca el ciclo completo: desde el diseño físico de hardware y soldadura de componentes hasta la implementación de una infraestructura de red robusta, servidores web seguros bajo **HTTPS/Cloudflare**, automatización de scripts en **Python** y un completo plan de empresa[cite: 2, 3, 4, 5].

---

## 🛠️ Stack Tecnológico & Componentes

### 🖥️ Hardware y Sensores
* **Cerebro:** Raspberry Pi 4 Modelo B (8GB RAM)[cite: 60].
* **Entorno & Luz:** Sensores **BME280** (Temperatura, Humedad, Presión) y **BH1750** (Luminosidad en Lux) por bus I2C[cite: 44, 45].
* **Viento y Lluvia:** Anemómetro, Veleta (con conversor analógico-digital **ADS1115**) y Pluviómetro de balancín[cite: 47, 48, 50].
* **Interfaz Visual:** Pantalla OLED I2C y Webcam USB para transmisión de imágenes en tiempo real[cite: 11, 52, 58].

### 💻 Software y Redes
* **Lenguaje:** Python (IoT, lectura de GPIOs mediante `gpiozero` y drivers de Adafruit)[cite: 65, 66, 68].
* **Servidor (Servidor Marta):** Linux Mint / Windows 11 sobre hardware dedicado[cite: 83, 85].
* **Servicios Web y Red:** Apache2 (Virtual Hosts, Módulo PAM), ProFTPD, SSH y Webmin protegido con **2FA (Google Authenticator)**[cite: 83, 87, 89, 123, 130].
* **Seguridad y DNS:** Cloudflare (CDN, túneles, reglas de seguridad y Turnstile Anti-Bot)[cite: 94, 96, 97, 118].
* **CMS:** WordPress maquetado con Elementor para el panel de clientes (*Mi Estación*)[cite: 102, 106].

---

## 📐 Esquema de Conexiones (Resumen)

| Componente | Protocolo / Bus | Pin / Puerto Principal |
| :--- | :--- | :--- |
| **BME280 / BH1750 / ADS1115** | I2C (SDA / SCL) | Pines físicos 3 y 5 de la Raspberry Pi[cite: 44, 59] |
| **Anemómetro** | GPIO digital | GPIO 5 (Pin 29)[cite: 49, 59] |
| **Pluviómetro** | GPIO digital | GPIO 6 (Pin 31)[cite: 51, 59] |
| **Cámara Web** | USB | Puerto USB 3.0[cite: 58, 61] |

---

## 🚀 Estructura del Repositorio y Automatización
Los scripts de la Raspberry Pi recogen las lecturas de los sensores, generan dinámicamente un archivo **JSON** y una plantilla en formato **TXT** compatible con la red *Meteoclimatic*, enviándolos de forma automatizada al Servidor Marta mediante **SCP**[cite: 78, 80].

---

## 👥 Equipo del Proyecto
* **Ximo Crespo Oltra** — *Coordinador del proyecto y Responsable de Software*[cite: 9]
* **Harmanpreet Singh Kaur** — *Responsable de Hardware, Electrónica y Soldadura*[cite: 9]
* **Borja Crespo Buigues** — *Responsable de Documentación y Seguridad*[cite: 9]
