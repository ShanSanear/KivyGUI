from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainContainer(BoxLayout):
    def __init__(self):
        self.properties_count = 0
        super(MainContainer, self).__init__()

    def add_new_property(self, text):
        print("Adding new property")
        tmp = 'property_' + str(self.properties_count)
        self.add_widget(SinglePropertyLayout(text, text), 2)
        self.properties_count += 1

    def callback_info(self, *args, **kwargs):
        print("IDs:", self.ids)
        print("Dict:", self.__dict__)
        print("Childs:", self.children)
        for child in self.children:
            if 'text_input_value' in child.ids:
                print(child.ids['text_input_value'])
            print(child.ids)


class OptionsContainer(BoxLayout):
    pass

class SinglePropertyLayout(BoxLayout):
    def __init__(self, element_id, provided_text):
        self.id = element_id
        super(SinglePropertyLayout, self).__init__()
        self.children[0].text = provided_text
        self.children[1].text = provided_text


class MyApp(App):

    def build(self):
        Window.size = (200, 300)
        root = MainContainer()
        root.orientation = 'vertical'
        print(root)
        return root


if __name__ == '__main__':
    MyApp().run()
    Config.set('kivy', 'keyboard_mode', 'system')
    Config.write()
