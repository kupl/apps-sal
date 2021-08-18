class Person:
    def __init__(self, name, my_family, gender='A'):
        self.name = name
        self.children = []
        self.parents = []
        self.cluster = {self, }
        self.gender = gender
        my_family.known_persons[name] = self


class family:
    def __init__(self):
        self.known_persons = {}

    @staticmethod
    def __opposite_gender__(gender):
        return {'M': 'F', 'F': 'M', 'A': 'B', 'B': 'A'}[gender]

    def __define_gender__(self, person, gender):
        if person in self.known_persons:
            if self.known_persons[person].gender in ('A', 'B'):
                original_gender = self.known_persons[person].gender
                opposite_new_gender = family.__opposite_gender__(gender)
                for p in self.known_persons[person].cluster:
                    p.gender = gender if p.gender == original_gender else opposite_new_gender
            else:
                return self.known_persons[person].gender == gender
        else:
            self.known_persons[person] = Person(person, gender=gender, my_family=self)
        return True

    def male(self, person):
        return self.__define_gender__(person, 'M')

    def female(self, person):
        return self.__define_gender__(person, 'F')

    def is_male(self, person):
        return person in self.known_persons and self.known_persons[person].gender == 'M'

    def is_female(self, person):
        return person in self.known_persons and self.known_persons[person].gender == 'F'

    def __is_ancestor_of__(self, p1, p2):
        if p1 == p2:
            return True
        elif len(p1.children) == 0:
            return False
        for c in p1.children:
            if self.__is_ancestor_of__(c, p2):
                return True
        return False

    @staticmethod
    def __join_cluster__(old_cluster, new_cluster, source_gender, target_gender, modify_genders=True):
        for p in old_cluster:
            if modify_genders:
                if p.gender == target_gender:
                    p.gender = family.__opposite_gender__(source_gender)
                else:
                    p.gender = source_gender
            new_cluster.add(p)
            p.cluster = new_cluster

    def set_parent_of(self, child, parent):
        if child == parent:
            return False
        if child not in self.known_persons:
            p = self.known_persons[parent] if parent in self.known_persons else Person(parent, my_family=self)
            c = Person(child, my_family=self)
        else:
            c = self.known_persons[child]
            if parent not in self.known_persons:
                if len(c.parents) >= 2:
                    return False
                p = Person(parent, my_family=self)
                if len(c.parents) == 1:
                    family.__join_cluster__(p.cluster, c.parents[0].cluster, c.parents[0].gender, p.gender)
            else:
                p = self.known_persons[parent]
                if c in p.children:
                    return True
                if len(c.parents) >= 2:
                    return False
                if self.__is_ancestor_of__(c, p):
                    return False
                if len(c.parents) == 1:
                    other_parent = c.parents[0]
                    if other_parent.cluster == p.cluster \
                            or other_parent.gender in ('M', 'F') and p.gender in ('M', 'F'):
                        if other_parent.gender == p.gender:
                            return False
                        elif other_parent.cluster != p.cluster:
                            family.__join_cluster__(p.cluster, other_parent.cluster,
                                                    other_parent.gender, p.gender,
                                                    modify_genders=False)
                    elif p.gender in ('A', 'B'):
                        family.__join_cluster__(p.cluster, other_parent.cluster, other_parent.gender, p.gender)
                    elif other_parent.gender in ('A', 'B'):
                        family.__join_cluster__(other_parent.cluster, p.cluster, p.gender, other_parent.gender)
                    else:
                        print("add_parent: unknown gender combination")
                        return False
        c.parents.append(p)
        p.children.append(c)
        return True

    def get_parents_of(self, person):
        return sorted([p.name for p in self.known_persons[person].parents]) if person in self.known_persons else []

    def get_children_of(self, person):
        return sorted([c.name for c in self.known_persons[person].children]) if person in self.known_persons else []
