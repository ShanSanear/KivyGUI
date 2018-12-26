from random import sample
from string import ascii_lowercase

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView


class RV(RecycleView):
    pass


class Row(BoxLayout):
    value = StringProperty()
    attr = StringProperty()
    attr_mod_val = StringProperty()

class Test(BoxLayout):

    def __init__(self):
        super(Test, self).__init__()
        self.rv.data = [{'value': val, 'attr': attr} for (val, attr) in
                        zip(['14'] * 6, ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'))]
        self.add_mods_to_attributes()
        self.rv.refresh_from_data()

    def add_ids_to_data(self, *args):
        print("adding ids")
        print(args)
        for child in self.rv.children[0].children:
            print(child)
            child.id = child.attr.lower() + '_id'
        print("Childs ids")
        for child in self.rv.children[0].children:
            print(child.id)

    def add_mods_to_attributes(self):
        for idx, attribute in enumerate(self.rv.data):
            attr_val = self.rv.data[idx]['value']
            mod = (int(attr_val) - 10) // 2
            sign = '-' if mod < 0 else '+'
            self.rv.data[idx]['attr_mod_val'] = sign + str(mod)

    def update_rv_data(self, rv_box_layout):
        print(rv_box_layout)
        print(self.ids.rv_box_layout.children)
        attr_updated_data = []
        for attribute_data in reversed(rv_box_layout.children):

            print(attribute_data.attr)
            print(attribute_data.value)
            attr_updated_data.append([attribute_data.value, attribute_data.attr])

        self.rv.data = [{'value': val, 'attr': attr} for (val, attr) in attr_updated_data]
        self.add_mods_to_attributes()


class AttributesApp(App):
    def build(self):
        test = Test()
        Clock.schedule_once(test.add_ids_to_data, 1)
        return test


if __name__ == '__main__':
    app = AttributesApp()
    app.run()
