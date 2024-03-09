from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from mydatabase import Database

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
<Signup>:
    name:"signup"
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
                orientation: "vertical"
                size_hint_y:None
                height:self.minimum_height
                spacing:dp(10)
                padding: [dp(30), 0, dp(30), 0]
                Label:
                    text: "Create your account"
                    size_hint_y: None
                    size: self.texture_size
                    halign:"left"
                    text_size: self.size
                    font_size: '16sp'
                    font_name: "robotoblack.ttf"
                CTextInput:
                    id: email
                    hint_text: "Username"
                    size_hint_y: None
                    height: dp(50)
                CTextInput:
                    id: password
                    hint_text: "Password"
                    size_hint_y: None
                    height: dp(50)
                    password: True
                CTextInput:
                    id: cpassword
                    hint_text: "Confirm Password"
                    size_hint_y: None
                    height: dp(50)
                    password: True
                CButton:
                    text: "Sign up"
                    size_hint_y: None
                    height: dp(50)
                    on_press: root.createEntry()
        AnchorLayout:
            size_hint:1,0.1
            anchor_x:"center"
            BoxLayout:
                size_hint_x:None
                width:self.minimum_width
                Label:
                    text:"You already have an account? "
                    size_hint_x:None
                    size:self.texture_size
                SignupText:
                    text:"Log in"
                    size_hint_x:None
                    size:self.texture_size
                    on_press: root.switchToLogin()

""")

class Signup(Screen):
    email=None
    password=None
    cpassword=None


    def createEntry(self):
        self.email = self.ids.email.text
        self.password=self.ids.password.text
        self.cpassword=self.ids.cpassword.text
        if (self.password==self.cpassword):
            if Database.isValid(self.email):
                Database.insertdata(self.email,self.password)
                self.manager.current="login"
            else:
                print("Email already exists")

    def switchToLogin(self):
        App.get_running_app().root.resetInputs()
        self.manager.current="login"