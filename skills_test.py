from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput


class SkillsMainContainer(BoxLayout):
    def __init__(self):
        super(SkillsMainContainer, self).__init__()
        print(self.ids.skills_rv_header)
        self.skills_rv_header.data = [
            {'skill_name': "Skill name", 'skill_attribute': "Attr", 'skill_full_mod': "Full mod",
             'skill_attribute_mod': "Attr mod", 'skill_rank': "Rank", 'skill_misc': "Misc",
             'skill_button': "Add / Remove"}]
        d = {'skill_name': "Dummy skill", 'skill_attribute': "STR", 'skill_full_mod': "+12",
             'skill_attribute_mod': "+2", 'skill_rank': "+8", 'skill_misc': "+2", 'skill_remove_add_text': 'remove'}
        d1 = dict(skill_name="", skill_attribute="", skill_full_mod="", skill_attribute_mod="",
                  skill_rank="", skill_misc="", skill_remove_add_text="Add")
        self.skills_rv.data = [d, d1]

    def add_or_remove_skill(self, single_skill_row):
        print()


    def add_new_skill(self):
        pass

    def remove_skill(self, skill_to_remove):
        pass


class SkillsRecycleView(RecycleView):
    skills_rv = ObjectProperty(None)


class SingleSkillRow(BoxLayout):
    def add_remove_skill_callback(self, root_reference):
        print("Callback from button")
        print(root_reference)


class SkillsApp(App):

    def build(self):
        root = SkillsMainContainer()
        print(root)
        return root


if __name__ == '__main__':
    SkillsApp().run()
