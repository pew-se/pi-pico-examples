import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import board
import digitalio

btn1_pin = board.GP6
btn2_pin = board.GP5
btn3_pin = board.GP4
btn4_pin = board.GP3
btn5_pin = board.GP2
btn6_pin = board.GP14
btn7_pin = board.GP26
btn8_pin = board.GP28
btn9_pin = board.GP27
btn10_pin = board.GP7

def button(btn_pin):
    btn = digitalio.DigitalInOut(btn_pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    return btn

btn1 = button(btn1_pin)
btn2 = button(btn2_pin)
btn3 = button(btn3_pin)
btn4 = button(btn4_pin)
btn5 = button(btn5_pin)
btn6 = button(btn6_pin)
btn7 = button(btn7_pin)
btn8 = button(btn8_pin)
btn9 = button(btn9_pin)
btn10 = button(btn10_pin)

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

MEDIA = 1
KEY = 2

while True:
    if btn1.value == 0:
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        time.sleep(0.1)
    if btn2.value == 0:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.1)
    if btn3.value == 0:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.1)
    if btn4.value == 0:
        keyboard.send(Keycode.K)
        keyboard.send(Keycode.A)
        keyboard.send(Keycode.T)
        keyboard.send(Keycode.T)
        keyboard.send(Keycode.SPACE)
        time.sleep(0.1)
    if btn5.value == 0:
        keyboard.send(Keycode.ENTER)
        time.sleep(0.1)
    if btn6.value == 0:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.1)
    if btn7.value == 0:
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.1)
    if btn8.value == 0:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)
    if btn9.value == 0:
        cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
        time.sleep(0.1)
    if btn10.value == 0:
        cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
        time.sleep(0.1)
    time.sleep(0.1)
