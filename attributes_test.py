from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView


class AttributesRecycleView(RecycleView):
    def update_rv_data(self, attributes_rows):
        attr_updated_data = []
        for attribute_data in reversed(attributes_rows):
            attr_updated_data.append([attribute_data.value, attribute_data.attr])
        self.data = [{'value': val, 'attr': attr} for (val, attr) in attr_updated_data]
        self.add_mods_to_attributes(1)
        self.refresh_from_data()

    def add_mods_to_attributes(self, time):
        for idx, attribute in enumerate(self.data):
            attr_val = self.data[idx]['value']
            mod = (int(attr_val) - 10) // 2
            self.data[idx]['attr_mod_val'] = '{:+d}'.format(mod)


class Row(BoxLayout):
    value = StringProperty()
    attr = StringProperty()
    attr_mod_val = StringProperty()


class AttributesMainContainer(BoxLayout):

    def __init__(self):
        super(AttributesMainContainer, self).__init__()
        self.attributes_rv_header.data = [{'attr_value': 'VALUE', 'attr_name': 'ATTRIBUTE', 'attr_mod': 'MOD'}]
        self.attributes_rv.data = [{'value': val, 'attr': attr} for (val, attr) in
                                   zip(['14'] * 6, ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'))]
        self.attributes_rv.add_mods_to_attributes(1)
        self.attributes_rv.refresh_from_data()

    def add_ids_to_data(self, *args):
        print("adding ids")
        print(args)
        for child in self.attributes_rv.children[0].children:
            print(child)
            child.id = child.attr.lower() + '_id'
        print("Childs ids")
        for child in self.attributes_rv.children[0].children:
            print(child.id)

    def update_rv_data(self, rv_box_layout):
        print(rv_box_layout)
        print(self.ids.rv_box_layout.children)
        self.attributes_rv.update_rv_data(self.ids.rv_box_layout.children)


class AttributesApp(App):
    def build(self):
        test = AttributesMainContainer()
        Clock.schedule_once(test.attributes_rv.add_mods_to_attributes, 1)
        Clock.schedule_once(test.add_ids_to_data, 1)
        return test


if __name__ == '__main__':
    app = AttributesApp()
    app.run()
