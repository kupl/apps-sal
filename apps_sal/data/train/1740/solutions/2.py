from enum import Enum


class Gender(Enum):
    FEMALE = 1
    MALE = 2

    @staticmethod
    def opp_gender(gender):
        opp = {Gender.MALE: Gender.FEMALE, Gender.FEMALE: Gender.MALE}
        return opp[gender]


class Person:
    def __init__(self, name):
        self.name = name
        self.gender = None
        self.children = []
        self.parents = []

    def __copy__(self):
        copy = Person(self.name)
        copy.gender = self.gender
        copy.children = self.children.copy()
        copy.parents = self.parents.copy()
        return copy

    def __str__(self):
        return "Name: {}, Gender: {}, Children: {}, Parents: {}".format(self.name, self.gender, self.children, self.parents)


class Family:

    def __init__(self):
        self.family = dict()

    def __copy__(self):
        copy = Family()
        copy.family = {name: person.__copy__() for name, person in list(self.family.items())}
        return copy

    def __str__(self):
        return "\n" + "\n".join(person.__str__() for name, person in list(self.family.items())) + "\n"

    def init_if_missing(self, name):
        if name not in self.family:
            self.family[name] = Person(name)

    def set_gender(self, name, gender):
        self.init_if_missing(name)
        if self.family[name].gender == gender:
            return True
        elif self.family[name].gender == Gender.opp_gender(gender):
            return False
        else:
            for child in self.family[name].children:
                for parent in self.family[child].parents:
                    if parent != name and self.family[parent].gender == gender:
                        return False
            self.family[name].gender = gender
            for child in self.family[name].children:
                self.update_parent_of(child)
            return True

    def male(self, name):
        return self.set_gender(name, Gender.MALE)

    def is_male(self, name):
        self.init_if_missing(name)
        return self.family[name].gender == Gender.MALE

    def female(self, name):
        return self.set_gender(name, Gender.FEMALE)

    def is_female(self, name):
        self.init_if_missing(name)
        return self.family[name].gender == Gender.FEMALE

    def set_parent_of(self, child_name, parent_name):
        self.init_if_missing(child_name)
        self.init_if_missing(parent_name)
        current_parents = self.get_parents_of(child_name)
        if parent_name in current_parents:
            return True

        elif parent_name == child_name \
            or child_name in self.get_ancestors_of(parent_name) \
            or 2 <= len(current_parents) \
            or (len(current_parents) == 1 and self.family[parent_name].gender is not None and
                self.family[current_parents[0]].gender == self.family[parent_name].gender):
            return False

        else:
            if len(current_parents) == 1 and self.family[parent_name].gender is None \
                    and self.family[current_parents[0]].gender is None:
                family_copy = self.__copy__()
                res = family_copy.female(parent_name)
                if res:
                    res = family_copy.set_parent_of(child_name, parent_name)
                    if not res:
                        return False

            self.update_parent_of(child_name, parent_name)
            return True

    def update_parent_of(self, child_name, parent_name=None):
        if parent_name is not None:
            self.family[child_name].parents.append(parent_name)
            self.family[parent_name].children.append(child_name)
            self.family[parent_name].children.sort()

        if len(self.family[child_name].parents) == 2:
            self.family[child_name].parents.sort()
            p0, p1 = self.family[self.family[child_name].parents[0]], self.family[self.family[child_name].parents[1]]
            if (p0.gender is not None and p1.gender is not None) or (p0.gender is None and p1.gender is None):
                return

            if p0.gender is not None:
                self.family[self.family[child_name].parents[1]].gender = Gender.opp_gender(p0.gender)
                for child in p1.children:
                    if child != child_name:
                        self.update_parent_of(child, None)
            elif p1.gender is not None:
                self.family[self.family[child_name].parents[0]].gender = Gender.opp_gender(p1.gender)
                for child in p0.children:
                    if child != child_name:
                        self.update_parent_of(child, None)

    def get_children_of(self, name):
        self.init_if_missing(name)
        return self.family[name].children.copy()

    def get_parents_of(self, name):
        self.init_if_missing(name)
        return self.family[name].parents.copy()

    def get_ancestors_of(self, name):
        self.init_if_missing(name)
        parents = self.get_parents_of(name)
        ln = len(parents)
        for parent in parents[:ln]:
            parents.extend(self.get_ancestors_of(parent))
        return parents
