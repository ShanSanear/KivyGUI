from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView


class FeatsMainContainer(BoxLayout):
    def __init__(self):
        super(FeatsMainContainer, self).__init__()
        self.feats_rv_header.data = [{'feat_name': "Feat", 'description_text': 'DESC', 'add_remove_button_text': "Add/Remove"}]
        self.feats_rv.data = [{'id': 'feat_0', 'description_text': 'DESC','feat_name': "OMG!", 'feat_add_remove_text': 'Remove'},
                              {'id': 'feat_-1', 'feat_name': "", 'feat_add_remove_text': 'Add'}]


class FeatsRecycleView(RecycleView):
    # TODO
    # This functionality below needs to be inherited from other class instead of almost copy-pasted from skills

    def add_or_remove_feat(self, single_feat_row):
        skill_id = single_feat_row.id
        if skill_id == "feat_-1":
            self.add_new_feat()
        else:
            print(single_feat_row.id)
            self.remove_feat(skill_id)
        self.refresh_from_data()

    def add_new_feat(self):
        print("Adding new skill")
        highest_id = self.get_all_feats_ids()

        new_skill_dummy = {'id': f'feat_{highest_id + 1}', 'feat_name': "Dummy feat",  'skill_remove_add_text': 'Remove'}
        self.data.insert(-1, new_skill_dummy)

    def get_all_feats_ids(self):
        ids = [int(feat['id'][5:]) for feat in self.data]
        highest_id = max(ids)
        return highest_id

    def remove_feat(self, feat_id):
        print("Removing feat")
        idx_to_delete = None
        for idx, element in enumerate(self.data):
            if element['id'] == feat_id:
                idx_to_delete = idx
        if idx_to_delete is not None:
            self.data.pop(idx_to_delete)
        else:
            print("Something went wrong")


class FeatsHeaderRecycleView(RecycleView):
    pass


class FeatsApp(App):
    def build(self):
        return FeatsMainContainer()


if __name__ == '__main__':
    FeatsApp().run()
