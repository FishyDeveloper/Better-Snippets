from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import pyautogui
import time

Config.set('graphics','width',500)
Config.set('graphics','height',400)
Config.set('graphics','resizable',False)

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')

class whatever(App):
    def build(self):
        return kv

whatever().run()