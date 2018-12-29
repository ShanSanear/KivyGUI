from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

from kivy_templates import BaseRecycleView


class FeatsMainContainer(BoxLayout):
    def __init__(self):
        super(FeatsMainContainer, self).__init__()
        self.feats_rv_header.data = [
            {'feat_name': "Feat", 'description_text': 'DESC', 'add_remove_button_text': "Add/Remove"}]
        self.feats_rv.data = [
            {'id': 'feat_0', 'description_text': 'DESC', 'feat_name': "OMG!", 'feat_add_remove_text': 'Remove'},
            {'id': 'feat_-1', 'feat_name': "", 'feat_add_remove_text': 'Add'}]


class FeatsRecycleView(BaseRecycleView):
    # TODO
    # This functionality below needs to be inherited from other class instead of almost copy-pasted from skills
    def __init__(self):
        super(FeatsRecycleView, self).__init__('feat',
                                               {'feat_name': "Dummy feat", 'button_text': 'Remove'})

    def add_or_remove_feat(self, single_feat_row):
        self.add_or_remove_element(single_feat_row)


class FeatsHeaderRecycleView(RecycleView):
    pass


class FeatsApp(App):
    def build(self):
        return FeatsMainContainer()


if __name__ == '__main__':
    FeatsApp().run()
