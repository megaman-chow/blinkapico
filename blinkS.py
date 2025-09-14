import machine
import time

# Define the pin for the LED
led = machine.Pin(25, machine.Pin.OUT)

# Timing constants (in seconds)
dot_duration = 0.2
dash_duration = dot_duration * 3
intra_char_pause = dot_duration
inter_char_pause = dot_duration * 3

def dot():
    led.on()
    time.sleep(dot_duration)
    led.off()
    time.sleep(intra_char_pause)

def dash():
    led.on()
    time.sleep(dash_duration)
    led.off()
    time.sleep(intra_char_pause)

def blink_S():
    dot()
    dot()
    dot()

# Main loop
while True:
    blink_S()
    time.sleep(inter_char_pause)

