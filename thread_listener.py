from pynput import keyboard
import threading
import sys

class TerminateListener:
    def __init__(self, driver):
        self.esc_pressed = False
        self.driver = driver

    def on_press(self, key):
        if key == keyboard.Key.esc:
            self.esc_pressed = True
    
    def esc_checker(self):
        while True:
            if self.esc_pressed:
                self.driver.quit()
                break
    
    def start_esc_checker(self):
        esc_thread = threading.Thread(target=self.esc_checker)
        esc_thread.start()
