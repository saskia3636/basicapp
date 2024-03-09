from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from styles import Styles

Builder.load_string("""
#: import CButton custom_widgets
<Home>:
    name: "Home"
    FloatLayout:
        Image:
            source: "vocsens.png"
            fit_mode: "contain"
            pos_hint: {"center_x":0.5, "top": 1.25}
        BoxLayout:
            orientation:"vertical"
            BoxLayout:
                canvas.before:
                    Color:
                        rgba: root.bg_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint_y:None
                height: dp(60)   
                AnchorLayout:
                    anchor_x: "left"
                    padding:[dp(20),0,0,0]
                    Button:
                        canvas.before:
                            Color:
                                rgba: root.bg_color
                            Rectangle:
                                pos: self.pos
                                size: self.size
                                source:"home.png"
                        size_hint:None,None
                        size: dp(35), dp(35)
                        background_normal: ""
                        background_color:0,0,0,0
                AnchorLayout:
                    anchor_x: "center"
                    Label:
                        text:"Home"
                        font_name: "robotoblack.ttf"
                AnchorLayout:
                    anchor_x: "right"
                    padding:[0,0,dp(20),0]
                    Button:
                        canvas.before:
                            Color:
                                rgba: root.bg_color
                            Rectangle:
                                pos: self.pos
                                size: self.size
                                source:"signout.jpg"
                        size_hint:None,None
                        size: dp(35), dp(35)
                        background_normal: ""
                        background_color:0,0,0,0
                        on_press: root.signout()
            BoxLayout:
                size_hint:1,0.45
            AnchorLayout:
                anchor_x: "center"
                anchor_y: "center"
                BoxLayout:
                    orientation:"vertical"
                    spacing:dp(20)
                    padding: dp(30)
                    BoxLayout:
                        size_hint:1,0.35
                        orientation:"vertical"
                        CButton:
                            text:"See graph"
                            font_name: "robotolight.ttf"
                            font_size: '18sp'
                            background_color: root.btn_color
                            on_press: root.showGraph()
                    BoxLayout:
                        size_hint:1,0.35
                        orientation:"vertical"
                        CButton:
                            text:"See data"
                            font_name: "robotolight.ttf"
                            font_size: '18sp'
                            background_color: root.btn_color
                    BoxLayout:
                        size_hint:1,0.30
                        orientation:"vertical"
                        padding: dp(30)
                        CButton:
                            text:"user settings"
                            font_size: '14sp'
                            font_name: "robotolight.ttf"
                            background_color: root.btn_color
        
        
""")

class Home(Screen):
    bg_color=Styles.primary_color
    btn_color=Styles.button_color
    text_color=Styles.secondary_color

    def signout(self):
        App.get_running_app().root.resetInputs()
        self.manager.current="login"

    def showGraph(self):
        self.manager.current="graph"