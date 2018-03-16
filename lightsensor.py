from gpiozero import LightSensor
sensor = LightSensor(18)
from time import sleep

while True:
    print(sensor.value)
    sleep(0.2)