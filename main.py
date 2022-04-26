from random import random
from tkinter import W
from urllib.parse import quote_plus
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import glob
from pathlib import Path
import random
from matplotlib.style import available


Builder.load_file('design.kv')

class LoginScreen(Screen):
    def signUp(self):
        self.manager.current = "Signup_Screen"
    
    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        
        if username in users and users[username]['password'] == password:
            self.manager.transition.direction = "left"
            self.manager.current= "Login_Success_Screen"
        else:
            self.ids.labelLoginError.text = "Incorrect username or password"




class SignupScreen(Screen):
    def addUser(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
            

        users[username] = {'username': username, 'password': password,
                                'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json",W) as file:
            json.dump(users, file)

        self.manager.current= "Signup_Success_Screen"

class SignupSuccessScreen(Screen):
    def go_to_login(self):

        self.manager.transition.direction = "right"
        self.manager.current = "login_Screen"

class LoginSuccessScreen(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_Screen"

    def getQuote(self, userInput):
        userInput=userInput.lower()
        availableFeelings = glob.glob("quotes/*txt")

        availableFeelings = [Path(filename).stem for filename in availableFeelings]
        
        if userInput in availableFeelings:
            with open(f"quotes/{userInput}.txt", encoding="utf8") as file:
                quotes = file.readlines()
                self.ids.labelQuote.text = random.choice(quotes)
        else:
            self.ids.labelQuote.text = "Try another feeling O.O"
    
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()