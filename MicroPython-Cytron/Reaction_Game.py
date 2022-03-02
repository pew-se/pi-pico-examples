### Reaction Game!
# Wait for led on GP15 to go dark, then race to press the button on either GP20 or GP21!
# Whoever presses the button fastest wins!
# The winners reaction time is printed in the shell

import machine
import utime
import urandom

pressed = False
led = machine.Pin(15, machine.Pin.OUT)
left_button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)
right_button = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
fastest_button = None
timer_reaction = None

def button_handler(pin):
    global pressed
    if not pressed:
        pressed=True
        global fastest_button
        fastest_button = pin
        global timer_reaction
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)

timer_start = utime.ticks_ms()
left_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)
right_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)

while fastest_button is None:
    utime.sleep(1)
if fastest_button is left_button:
    print("Left player wins with reaction time of " + str(timer_reaction) + " milliseconds!")
elif fastest_button is right_button:
    print("Right player wins with reaction time of " + str(timer_reaction) + " milliseconds!")