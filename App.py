from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooser
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import pyautogui
import time

Config.set('graphics','width',500)
Config.set('graphics','height',400)
Config.set('graphics','resizable',False)

class FileChooserPopUp(Screen):
    SelectedFile = ObjectProperty(None)


class FirstScreen(Screen):
    def toggle_theme(self):
        print('works?')

class SecondScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('App.kv')

class whatever(App):
    def build(self):
        return kv

whatever().run()