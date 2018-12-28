from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView


class SkillsMainContainer(BoxLayout):
    def __init__(self):
        super(SkillsMainContainer, self).__init__()
        default_skills_rv_header_data = [
            {'skill_name': "Skill name", 'skill_attribute': "Attr", 'skill_full_mod': "Full mod",
             'skill_attribute_mod': "Attr mod", 'skill_rank': "Rank", 'skill_misc': "Misc",
             'skill_button': "Add / Remove"}]
        self.skills_rv_header.data = default_skills_rv_header_data
        template_skill = {'id': "skill_0", 'skill_name': "Dummy skill", 'skill_attribute': "STR",
                          'skill_full_mod': "+12",
                          'skill_attribute_mod': "+2", 'skill_rank': "+8", 'skill_misc': "+2",
                          'skill_remove_add_text': 'Remove'}
        add_new_skill_row = dict(id='skill_-1', skill_name="", skill_attribute="", skill_full_mod="",
                                 skill_attribute_mod="",
                                 skill_rank="", skill_misc="", skill_remove_add_text="Add")
        self.skills_rv.data = [template_skill, add_new_skill_row]


class SkillsRecycleView(RecycleView):
    skills_rv = ObjectProperty(None)

    def add_or_remove_skill(self, single_skill_row):
        skill_id = single_skill_row.id
        if skill_id == "skill_-1":
            self.add_new_skill()
        else:
            print(single_skill_row.id)
            self.remove_skill(skill_id)
        self.refresh_from_data()

    def add_new_skill(self):
        print("Adding new skill")
        highest_id = self.get_all_skills_ids()

        new_skill_dummy = {'id': f'skill_{highest_id + 1}', 'skill_name': "Dummy skill", 'skill_attribute': "",
                           'skill_full_mod': "",
                           'skill_attribute_mod': "", 'skill_rank': "", 'skill_misc': "",
                           'skill_remove_add_text': 'Remove'}
        self.data.insert(-1, new_skill_dummy)

    def get_all_skills_ids(self):
        ids = [int(skill['id'][6:]) for skill in self.data]
        highest_id = max(ids)
        return highest_id

    def remove_skill(self, skill_id):
        print("Removing skill")
        idx_to_delete = None
        for idx, element in enumerate(self.data):
            if element['id'] == skill_id:
                idx_to_delete = idx
        if idx_to_delete is not None:
            self.data.pop(idx_to_delete)
        else:
            print("Something went wrong")


class SkillsApp(App):

    def build(self):
        root = SkillsMainContainer()
        return root


if __name__ == '__main__':
    SkillsApp().run()
