# System imports
import socket
import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch
import version as ver

def blink_led(delay, duration=10):
    # Led Blink
    start_time = time.time()

    while True:
        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)

        if time.time() - start_time >= duration:
            break

def main():
    switch.init()
    led.init()
    while True:
        if switch.read_slide_switch() == 1:
            blink_led(0.2)
        else:
            blink_led(0.1, 5)

# Main entry point
if __name__ == "__main__":
    main()