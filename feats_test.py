from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView

from kivy_templates import BaseRecycleView, PopupWithText


class FeatsPopup(PopupWithText):
    def __init__(self, feat_data, selected_feat_row, **kwargs):
        self.selected_feat = selected_feat_row
        self.feat_data = feat_data
        super(FeatsPopup, self).__init__(**kwargs)

    def dismissing(self):
        print("Dissmissing popup")
        new_desc = self.ids.container.children[0].content_text
        print(self.selected_feat.description_text)
        self.feat_data['description_text'] = new_desc

        print("Feat selected:", self.selected_feat)


class FeatsMainContainer(BoxLayout):
    def __init__(self, **kwargs):
        super(FeatsMainContainer, self).__init__(**kwargs)
        self.feats_rv_header.data = [
            {'feat_name': "Feat", 'description_text': 'DESC', 'add_remove_button_text': "Add/Remove"}]
        self.feats_rv.data = [
            {'id': 'feat_0', 'description_text': 'This is quite long description ' * 12, 'feat_name': "OMG!",
             'button_text': 'Remove'},
            {'id': 'feat_-1', 'description_text': "", 'feat_name': "", 'button_text': 'Add'}]


class FeatsRecycleView(BaseRecycleView):
    def __init__(self, **kwargs):
        super(FeatsRecycleView, self).__init__('feat',
                                               {'description_text': 'DESC', 'feat_name': "",
                                                'button_text': 'Remove'}, **kwargs)
        self.selected_feat = ObjectProperty()

    def add_or_remove_feat(self, single_feat_row):
        self.add_or_remove_element(single_feat_row)

    def show_description(self, single_feat_row):
        print("Showing desc")
        feat_data = self.get_element_with_id(single_feat_row.id)
        p = FeatsPopup(feat_data=feat_data, selected_feat_row=single_feat_row, title=single_feat_row.feat_name)
        p.ids.container.children[0].content_text = single_feat_row.description_text
        p.open()
        print("popup closed")


class FeatsHeaderRecycleView(RecycleView):
    pass


class FeatsApp(App):
    def build(self):
        return FeatsMainContainer()


if __name__ == '__main__':
    FeatsApp().run()
