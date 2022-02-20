from machine import Pin, ADC
import utime

# Connect joystick like this:
# GND -> pin 38 (gnd)
# +5V -> pin 36 (3v3 out)
# VRX -> pin 31 (ADC0 / gp26)
# VRY -> pin 32 (ADC1 / gp27)
# SW  -> pin 29 (gp22)

xAxis = ADC(Pin(26))
yAxis = ADC(Pin(27))
button = Pin(22, Pin.IN, Pin.PULL_UP)

def isPressed(int):
    if int == 0:
        return "pressed"
    else:
        return "not pressed"

def xDirection(value):
    if value < 5000:
        return "left"
    elif value > 60535:
        return "right"
    else:
        return "middle"

def yDirection(value):
    if value < 5000:
        return "up"
    elif value > 60535:
        return "down"
    else:
        return "middle"

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
#    print(str(xValue) +", " + str(yValue) + " -- " + str(button.value()))
    # nicer print values
    print(xDirection(xValue) +", " + yDirection(yValue) + " -- " + isPressed(button.value()))
    utime.sleep(0.1)