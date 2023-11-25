import RPi.GPIO as GPIO
import time

# Configura el modo de la GPIO
GPIO.setmode(GPIO.BCM)

# Configura el número del pin GPIO que deseas usar
led_pin = 18

# Configura el pin como salida
GPIO.setup(led_pin, GPIO.OUT)

while True:
    # Enciende el LED
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1)  # Espera 1 segundo

    # Apaga el LED
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(1)  # Espera 1 segundo