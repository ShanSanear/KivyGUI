from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class MainAcBox(BoxLayout):
    pass


class AcApp(App):
    def build(self):
        return MainAcBox()


if __name__ == '__main__':
    Window.size = [350, 100]
    AcApp().run()
