import array, utime
from machine import Pin
import neopixel

# Configure number of WS2812 LEDs.
NUM_LEDS = 1

button_r = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_g = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)

led_r = False
led_g = False
led_b = False
def button_handler(pin):
    if pin == button_r:
        global led_r
        if led_r == False:
            led_r = True
        else:
            led_r = False
        print("r toggle: " + str(led_r))
    if pin == button_g:
        global led_g
        if led_g == False:
            led_g = True
        else:
            led_g = False
        print("g toggle: " + str(led_g))
    if pin == button_b:
        global led_b
        if led_b == False:
            led_b = True
        else:
            led_b = False
        print("b toggle: " + str(led_b))
button_r.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
button_g.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
button_b.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)

neoPixel = neopixel.NeoPixel(machine.Pin(28), NUM_LEDS, bpp=4)

BRIGHTNESS_LEVEL = 64
def getBrightness(color):
    if color:
        return BRIGHTNESS_LEVEL
    else:
        return 0

print("now you go! Use buttons on GP20, GP21, GP22!")
while True:
    brightness = 0
    if led_r:
        brightness = 64
    elif led_g:
        brightness = 64
    elif led_b:
        brightness = 64
    neoPixel[0] = (getBrightness(led_r), getBrightness(led_g), getBrightness(led_b), brightness)
    neoPixel.write() # Output the colors to the led(s)
