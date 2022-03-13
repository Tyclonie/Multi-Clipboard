import time
import keyboard
import clipboard


class ClipBoard:
    def __init__(self):
        self.data = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 0: None}

    def get_value(self, number):
        return self.data[number]

    def set_value(self, number, data):
        self.data[number] = data


class App(ClipBoard):
    def __init__(self):
        super().__init__()
        while True:
            if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt") and keyboard.is_pressed("q"):
                if keyboard.is_pressed("1"):
                    self.enter_value(1)
                elif keyboard.is_pressed("2"):
                    self.enter_value(2)
                elif keyboard.is_pressed("3"):
                    self.enter_value(3)
                elif keyboard.is_pressed("4"):
                    self.enter_value(4)
                elif keyboard.is_pressed("5"):
                    self.enter_value(5)
                elif keyboard.is_pressed("6"):
                    self.enter_value(6)
                elif keyboard.is_pressed("7"):
                    self.enter_value(7)
                elif keyboard.is_pressed("8"):
                    self.enter_value(8)
                elif keyboard.is_pressed("9"):
                    self.enter_value(9)
                elif keyboard.is_pressed("0"):
                    self.enter_value(0)
            if keyboard.is_pressed("ctrl") and keyboard.is_pressed("c"):
                data = clipboard.paste()
                if keyboard.is_pressed("1"):
                    self.set_value(1, data)
                elif keyboard.is_pressed("2"):
                    self.set_value(2, data)
                elif keyboard.is_pressed("3"):
                    self.set_value(3, data)
                elif keyboard.is_pressed("4"):
                    self.set_value(4, data)
                elif keyboard.is_pressed("5"):
                    self.set_value(5, data)
                elif keyboard.is_pressed("6"):
                    self.set_value(6, data)
                elif keyboard.is_pressed("7"):
                    self.set_value(7, data)
                elif keyboard.is_pressed("8"):
                    self.set_value(8, data)
                elif keyboard.is_pressed("9"):
                    self.set_value(9, data)
                elif keyboard.is_pressed("0"):
                    self.set_value(0, data)

    def enter_value(self, index):
        value = self.get_value(index)
        if value is not None:
            keyboard.press("backspace")
            keyboard.write(value)
            time.sleep(0.3)

if __name__ == "__main__":
    App()
