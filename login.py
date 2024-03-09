from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from mydatabase import Database

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
#: import SignupText custom_widgets
<Login>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        padding:dp(20)
        BoxLayout:
            size_hint:1,0.35
            Image:
                source: "vocsens.png"
        AnchorLayout:
            size_hint:1,0.55 
            anchor_y:"top"
            BoxLayout:
                orientation:"vertical"
                size_hint_y:None
                height:self.minimum_height
                spacing:dp(10)
                padding: [dp(30), 0, dp(30), 0]
                Label:
                    text: "Log in to your Account"
                    font_size: '16sp'
                    font_name: "robotoblack.ttf"
                    text_size: self.size
                    size_hint_y:None
                    size:self.texture_size
                CTextInput:
                    id: email
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Username"
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Password"
                    password: True
                CButton:
                    size_hint_y: None
                    height: dp(50)
                    text: "Login"
                    on_press: root.login()
        AnchorLayout:
            size_hint:1,0.1
            anchor_x:"center"
            BoxLayout:
                size_hint_x:None
                width:self.minimum_width
                Label:
                    text:"Don't have an account? "
                    size_hint_x:None
                    size:self.texture_size
                SignupText:
                    text:"Sign up"
                    size_hint_x:None
                    size:self.texture_size
                    on_press: root.switchToSignup()
                
                

""")

class Login(Screen):
    email=None
    password=None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.email.text=""
        print("empty")

    def login(self):
        self.email = self.ids.email.text
        self.password = self.ids.password.text
        if Database.isExist(self.email, self.password):
            print("Login successful")
            self.manager.current="Home"
        else:
            print("Login failed")

    def switchToSignup(self):
        App.get_running_app().root.resetInputs()
        self.manager.current="signup"