from kivy.uix.recycleview import RecycleView


class BaseRecycleView(RecycleView):
    def __init__(self, element_string, row_data):
        super(BaseRecycleView, self).__init__()
        self.element_string = element_string
        self.element_string_len = len(self.element_string)
        self.row_data = row_data

    def add_or_remove_element(self, row_of_element):
        element_id = row_of_element.id
        if element_id == f'{self.element_string}_-1':
            self.add_new_element()
        else:
            self.remove_element(element_id)
        self.refresh_from_data()

    def add_new_element(self):
        highest_id = self.get_highest_id()
        new_element_dummy = {'id': f'{self.element_string}_{highest_id + 1}'}.update(self.row_data)
        self.data.insert(-1, new_element_dummy)

    def remove_element(self, element_id):
        idx_to_delete = None
        for idx, element in enumerate(self.data):
            if element['id'] == element_id:
                idx_to_delete = idx
        if idx_to_delete is not None:
            self.data.pop(idx_to_delete)
        else:
            print("Something went wrong")

    def get_highest_id(self):
        ids = [int(element['id'][self.element_string_len + 1]) for element in self.data]
        return max(ids)
