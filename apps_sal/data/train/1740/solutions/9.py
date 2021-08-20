from collections import defaultdict
from copy import deepcopy


class family:

    def __init__(self):
        self.fam = defaultdict(lambda: defaultdict(set))

    def male(self, name):
        return self.change_gender(name, 'male')

    def is_male(self, name):
        return self.fam[name]['gender'] == 'male'

    def female(self, name):
        return self.change_gender(name, 'female')

    def is_female(self, name):
        return self.fam[name]['gender'] == 'female'

    def set_parent_of(self, child_name, parent_name):
        if parent_name in self.fam[child_name]['parents']:
            return True
        if not self.check_parent(child_name, parent_name):
            return False
        res = True
        if self.fam[child_name]['parents']:
            other = next(iter(self.fam[child_name]['parents']))
            if self.fam[parent_name]['gender']:
                if self.fam[other]['gender']:
                    res = self.fam[parent_name]['gender'] != self.fam[other]['gender']
                else:
                    res = self.change_gender(other, family.opposite(self.fam[parent_name]['gender']))
            elif self.fam[other]['gender']:
                res = self.change_gender(parent_name, family.opposite(self.fam[other]['gender']))
            else:
                save = deepcopy(self.fam)
                self.fam[child_name]['parents'].add(parent_name)
                self.fam[parent_name]['children'].add(child_name)
                res = self.check_gender(parent_name) and self.check_gender(other)
                if not res:
                    self.fam = save
                return res
        if res:
            self.fam[child_name]['parents'].add(parent_name)
            self.fam[parent_name]['children'].add(child_name)
        return res

    def get_children_of(self, name):
        return sorted(self.fam[name]['children'])

    def get_parents_of(self, name):
        return sorted(self.fam[name]['parents'])

    def change_gender(self, name, gender):
        save = deepcopy(self.fam)
        if not self.update_gender(name, gender):
            self.fam = save
            return False
        return True

    def search_ancestors(self, name, search):
        if name == search:
            return True
        return any((self.search_ancestors(parent, search) for parent in self.fam[name]['parents']))

    def update_gender(self, name, gender):
        if self.fam[name]['gender']:
            return self.fam[name]['gender'] == gender
        self.fam[name]['gender'] = gender
        for child in self.fam[name]['children']:
            if len(self.fam[child]['parents']) == 2:
                other = next((p for p in self.fam[child]['parents'] if p != name))
                if not self.update_gender(other, family.opposite(gender)):
                    return False
        return True

    def check_gender(self, name):
        save = deepcopy(self.fam)
        res = self.update_gender(name, 'male')
        self.fam = save
        if res:
            return True
        save = deepcopy(self.fam)
        res = self.update_gender(name, 'female')
        self.fam = save
        return res

    def check_parent(self, child, parent):
        if child == parent:
            return False
        if len(self.fam[child]['parents']) == 2:
            return False
        if self.search_ancestors(parent, child):
            return False
        return True

    @staticmethod
    def opposite(gender):
        return 'female' if gender == 'male' else 'male'
