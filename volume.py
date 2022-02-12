from pynput.keyboard import Key, Controller
import keyboard
import time


keyboar = Controller()


while True:
    if keyboard.is_pressed("q+plus"):
        keyboar.press(Key.media_volume_up)
        keyboar.release(Key.media_volume_up)
        time.sleep(0.06)
    if keyboard.is_pressed("q+-"):
        keyboar.press(Key.media_volume_down)
        keyboar.release(Key.media_volume_down)
        time.sleep(0.06)
    if keyboard.is_pressed("q+end"):
        break
    time.sleep(0.009)
