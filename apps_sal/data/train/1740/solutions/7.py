from collections import deque
from enum import Enum


class Gender(Enum):
    Male = "M"
    Female = "F"


class Member:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.spouse = None
        self.gender = None

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"[{self.name}|{self.gender}<=>{self.spouse.name if self.spouse is not None else '?'}: {list(map(lambda c: c.name, self.children))}]"

    def set_gender(self, gender):
        if self.gender is not None and gender != self.gender:
            return False

        if self.spouse is not None:
            if self.spouse.gender == gender:
                return False
            else:
                if gender == Gender.Male:
                    self.spouse.gender = Gender.Female
                else:
                    self.spouse.gender = Gender.Male

        if self.gender is None:
            self.gender = gender
        return True

    def set_parent(self, parent):
        if parent not in self.parents:
            self.set_spouse(parent)
            self.parents.append(parent)

    def set_spouse(self, parent):
        if len(self.parents) == 1:
            current_parent = self.parents[0]
            parent.spouse = current_parent
            current_parent.spouse = parent

    def set_child(self, child):
        if child not in self.children:
            self.children.append(child)


class family:
    def __init__(self):
        self.members = []

    def is_male(self, name):
        member = self.add_member(name)
        return True if member.gender == Gender.Male else False

    def is_female(self, name):
        member = self.add_member(name)
        return True if member.gender == Gender.Female else False

    def male(self, name):
        member = self.add_member(name)

        if member.set_gender(Gender.Male):
            self.update_genders()
            return True
        else:
            return False

    def female(self, name):
        member = self.add_member(name)

        if member.set_gender(Gender.Female):
            self.update_genders()
            return True
        else:
            return False

    def set_parent_of(self, child_name, parent_name):
        child = self.add_member(child_name)
        parent = self.add_member(parent_name)

        if not self.valid_relationship(child, parent):
            return False

        child.set_parent(parent)
        parent.set_child(child)
        self.update_genders()
        return True

    def update_genders(self):
        for m in self.members:
            if m.spouse is not None and m.spouse.gender is not None:
                if m.spouse.gender == Gender.Male:
                    m.gender = Gender.Female
                else:
                    m.gender = Gender.Male

    def get_children_of(self, name):
        member = self.add_member(name)
        return sorted(list([m.name for m in member.children]))

    def get_parents_of(self, name):
        member = self.add_member(name)
        return sorted(list([m.name for m in member.parents]))

    def valid_relationship(self, child, parent):
        if child == parent:
            return False

        if child in parent.children:
            return True

        if not self.check_children_of_children(child, parent):
            return False

        if len(child.parents) >= 2:
            return False

        if len(child.parents) == 1:
            current_parent = child.parents[0]
            if current_parent.gender == parent.gender and current_parent.gender is not None:
                return False

        if not self.check_gender_assignment(child, parent):
            return False

        return True

    # BFS algorithm
    def check_gender_assignment(self, child, parent):
        visited = set()
        queue = deque([parent])
        visited.add(parent)

        counter = 1

        while queue:
            p = queue.popleft()

            if len(p.children) == 0:
                continue

            for c in p.children:
                if c not in visited:
                    visited.add(p)
                    for pp in c.parents:
                        if pp not in visited:
                            visited.add(pp)
                            queue.append(pp)
                            if pp.gender is None:
                                counter += 1

            # Detect cycle
            if child in p.children:
                if counter > 2:
                    if counter % 2 != 0 or counter > 5:
                        return False
        return True

    def check_children_of_children(self, child, parent):
        visited = set()
        queue = deque([child])
        visited.add(child)

        while queue:
            c = queue.popleft()
            
            if len(c.children) == 0:
                continue

            for cc in c.children:
                if cc == parent:
                    return False
                  
                if cc not in visited:
                    visited.add(cc)
                    queue.append(cc)
        
        return True

    def add_member(self, name):
        new_member = Member(name)
        if new_member not in self.members:
            self.members.append(new_member)
        return self.members[self.members.index(new_member)]

