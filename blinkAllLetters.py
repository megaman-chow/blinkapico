import machine
import time

# LED pin (for Pico's built-in LED, use pin 25)
led = machine.Pin(25, machine.Pin.OUT)

# Timing (seconds)
DOT = 0.2
DASH = DOT * 3
INTRA_CHAR = DOT          # between dots/dashes in the same letter
INTER_CHAR = DOT * 3      # between letters
WORD_PAUSE = DOT * 7      # between words

# Morse code dictionary
MORSE_CODE = {
    "A": ".-",    "B": "-...",  "C": "-.-.", "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",  "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",  "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",  "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",  "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",  "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

# Functions
def dot():
    led.on()
    time.sleep(DOT)
    led.off()
    time.sleep(INTRA_CHAR)

def dash():
    led.on()
    time.sleep(DASH)
    led.off()
    time.sleep(INTRA_CHAR)

def blink_char(char):
    code = MORSE_CODE.get(char.upper())
    if not code:
        return
    for symbol in code:
        if symbol == ".":
            dot()
        elif symbol == "-":
            dash()
    time.sleep(INTER_CHAR - INTRA_CHAR)  # adjust spacing at end of letter

def blink_message(message):
    for word in message.split(" "):
        for char in word:
            blink_char(char)
        time.sleep(WORD_PAUSE - INTER_CHAR)

# Example: blink "HELLO WORLD"
while True:
    blink_message("HELLO WORLD")
    time.sleep(3)
