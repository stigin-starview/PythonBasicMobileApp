from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('design.kv')

class LoginScreen(Screen):
    def signUp(self):
        self.manager.current = "SignupScreen"

class SignupScreen(Screen):
    def addUser(self, username, password):
        print(username,password)
    
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()