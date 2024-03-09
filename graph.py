from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np


from styles import Styles

Builder.load_string("""
#: import CButton custom_widgets
<Graph>:
    name: "graph"
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
                    on_press: root.goHome()
            AnchorLayout:
                anchor_x: "center"
                Label:
                    text:"Graph"
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
                            source:"list.png"
                    size_hint:None,None
                    size: dp(35), dp(35)
                    background_normal: ""
                    background_color:0,0,0,0
        BoxLayout:
            size_hint:1,0.25
            Label:
                text:"NH3 concentration"
                font_name: "robotoblack.ttf"
        AnchorLayout:
            anchor_x: "center"
            anchor_y: "center"
            padding: dp(10)
            BoxLayout:
                id:graphplaceholder
        BoxLayout:
            size_hint:1,0.25
            spacing:dp(20)
            padding: dp(30)
            Button:
                text:"update"
                font_name: "robotolight.ttf"
                font_size: '18sp'
                background_color: root.btn_color
                on_press:root.updateGraph()

""")

class Graph(Screen):
    bg_color=Styles.primary_color
    btn_color=Styles.button_color
    text_color=Styles.secondary_color

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        graph = self.createGraph()
        self.ids.graphplaceholder.add_widget(FigureCanvasKivyAgg(graph.gcf()))

    def createGraph(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]

        # Plot erstellen
        plt.plot(x, y)

        # Beschriftungen hinzufügen
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.title('Simple plot')

        return plt

    def updateGraph(self):
        x = [1, 2, 3, 4, 5]
        y = np.random.randint(0, 30, size=5)

        plt.clf()

        # Plot erstellen
        plt.plot(x, y)

        # Beschriftungen hinzufügen
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.title('Simple plot')
        children = self.ids.graphplaceholder.children
        if children:
            self.ids.graphplaceholder.remove_widget(children[0])
        self.ids.graphplaceholder.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        children = self.ids.graphplaceholder.children
        if children:
            self.ids.graphplaceholder.remove_widget(children[0])
        self.ids.graphplaceholder.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def goHome(self):
        self.manager.current="Home"

