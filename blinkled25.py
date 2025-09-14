import machine
import time

led = machine.Pin(25, machine.Pin.OUT)
while True:
    led.value(1)
    print("led on")
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
    

