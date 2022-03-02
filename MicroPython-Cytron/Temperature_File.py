# Logs temperature to "temps.txt" on the pico once per second, until the stop-button (GP20) is pressed.


import machine
import utime

stop_button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)

conversion_factor = 3.3 / 65535

def getTemperature():
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    return temperature

# Creates or overwrites file
file = open("temps.txt", "w")

while stop_button.value() != 0:
    file.write(str(getTemperature()) + "c\n")
    file.flush()
    print("tick")
    utime.sleep(1)

file.close()