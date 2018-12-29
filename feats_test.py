from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView

from kivy_templates import BaseRecycleView, PopupWithText


class FeatsMainContainer(BoxLayout):
    def __init__(self, **kwargs):
        super(FeatsMainContainer, self).__init__(**kwargs)
        self.feats_rv_header.data = [
            {'feat_name': "Feat", 'description_text': 'DESC', 'add_remove_button_text': "Add/Remove"}]
        self.feats_rv.data = [
            {'id': 'feat_0', 'description_text': 'This is quite long description '*12, 'feat_name': "OMG!", 'button_text': 'Remove'},
            {'id': 'feat_-1', 'description_text': "", 'feat_name': "", 'button_text': 'Add'}]


class FeatsRecycleView(BaseRecycleView):
    def __init__(self, **kwargs):
        super(FeatsRecycleView, self).__init__('feat',
                                               {'description_text': 'DESC', 'feat_name': "",
                                                'button_text': 'Remove'}, **kwargs)

    def add_or_remove_feat(self, single_feat_row):
        self.add_or_remove_element(single_feat_row)

    def show_description(self, single_feat_row):
        print("Showing desc")
        p = FeatsPopup(title=single_feat_row.feat_name)
        p.ids.container.children[0].content_text = single_feat_row.description_text
        p.open()

class FeatsPopup(PopupWithText):
    def __init__(self, **kwargs):
        super(FeatsPopup, self).__init__(**kwargs)


class FeatsHeaderRecycleView(RecycleView):
    pass


class FeatsApp(App):
    def build(self):
        return FeatsMainContainer()


if __name__ == '__main__':
    FeatsApp().run()
