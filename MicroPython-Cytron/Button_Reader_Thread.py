import machine
import utime
import _thread

button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_external = machine.Pin(15, machine.Pin.OUT)
led_buzz = machine.Pin(9, machine.Pin.OUT)

button_buzz = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
buzzer = machine.Pin(18, machine.Pin.OUT)

global button_pressed
button_pressed = False

while True:
    if button.value() == 0:
        led_external.value(1)
        utime.sleep(1)
    led_external.value(0)
    
    if button_pressed == True:
        led_buzz.value(1)
        print("herp derp")
    if button_buzz.value() == 0:
        buzzer.value(1)
        utime.sleep(0.2)
        buzzer.value(0)
        utime.sleep(0.2)

def button_reader_thread():
    global button_pressed
    while True:
        if button_buzz.value() == 1:
            button_pressed = True
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        utime.sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())