from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainSkillContainer(BoxLayout):
    def __init__(self):
        skill_name = ObjectProperty(None)
        main_skill_container = ObjectProperty(None)
        skill_attribute = ObjectProperty(None)
        super(MainSkillContainer, self).__init__()

class SkillTextInput(TextInput):
    pass


class OptionsContainer(BoxLayout):

    def __init__(self):
        self.properties_count = 0
        super(OptionsContainer, self).__init__()
        self.f = Factory

    def add_new_skill(self, skill_name, skill_attribute, main_skill_container):
        print(skill_name)
        print("Adding new skill")
        tmp = 'property_' + str(self.properties_count)
        main_skill_container.add_widget(SingleSkillLayout(tmp, skill_name, skill_attribute), 2)
        self.properties_count += 1

    def callback_info(self, *args, **kwargs):
        print("IDs:", self.ids)
        print("Dict:", self.__dict__)
        print("Children:", self.children)
        for child in self.children:
            if 'skill_attribute_label' in child.ids:
                print(child.ids['skill_attribute_label'])
            print(child.ids)


class SingleSkillLayout(BoxLayout):
    def __init__(self, element_id, skill_name, skill_attribute):
        self.id = element_id
        super(SingleSkillLayout, self).__init__()
        skill_name_text_input = self.ids['skill_name_label']
        skill_attribute_text_input = self.ids['skill_attribute_label']
        skill_name_text_input.text = skill_name
        skill_attribute_text_input.text = skill_attribute

    def show_skill(self):
        for child in self.children:
            print(child, child.text)


class SkillsApp(App):

    def build(self):
        Window.size = (800, 600)
        root = MainSkillContainer()
        root.orientation = 'vertical'
        root.add_widget(OptionsContainer())
        print(root)
        return root


if __name__ == '__main__':
    SkillsApp().run()
    Config.set('kivy', 'keyboard_mode', 'system')
    Config.write()
