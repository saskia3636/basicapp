from kivy.app import App
from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager

from graph import Graph
from login import Login
from signup import Signup
from mydatabase import Database
from home import Home

Window.softinput_mode="below_target"
#Window.size=(400,700)
class Interface(ScreenManager):
    login = None
    signup = None
    home = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            Database.connectDatabase()
        except Exception as e:
            print(e)

        self.login = Login()
        self.signup = Signup()
        self.home=Home()

        graph = Graph()

        self.add_widget(self.login)
        self.add_widget(self.signup)
        self.add_widget(self.home)
        self.add_widget(graph)

    def resetInputs(self):
        self.login.ids.email.text = ""
        self.login.ids.password.text=""

        self.signup.ids.email.text =""
        self.signup.ids.password.text =""
        self.signup.ids.cpassword.text =""

class BasisApp(App):
    pass


BasisApp().run()