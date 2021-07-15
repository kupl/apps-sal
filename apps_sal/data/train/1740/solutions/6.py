from collections import defaultdict

class family:
    def __init__(self):
        self.males = set()
        self.females = set()
        self.parents = defaultdict(lambda: set())
        self.children = defaultdict(lambda: set())
        
    def male(self, name):
        if name in self.females:
            return False
        if name in self.males:
            return True
        safe_copy = self.males.copy()
        self.males.add(name)
        for child in self.parents[name]:
            partners = self.children[child] - {name}
            for partner in partners:
                if not self.female(partner):
                    self.males = safe_copy
                    return False
        return True
    def is_male(self, name):
        return name in self.males
    def female(self, name):
        if name in self.males:
            return False
        if name in self.females:
            return True
        safe_copy = self.females.copy()
        self.females.add(name)
        for child in self.parents[name]:
            partners = self.children[child] - {name}
            for partner in partners:
                if not self.male(partner):
                    self.females = safe_copy
                    return False
        return True
    def is_female(self, name):
        return name in self.females
    def set_parent_of(self, child_name, parent_name):
        if child_name == parent_name:
            return False
        parents = self.children[parent_name]
        while parents:
            if child_name in parents:
                return False
            new_parents = set()
            for parent in parents:
                new_parents |= self.children[parent]
            parents = new_parents
        current_parents = self.children[child_name]
        if parent_name in current_parents:
            return True
        if len(current_parents) >= 2:
            return False
        new_parents = current_parents | {parent_name}
        if len(new_parents & self.males) > 1 or len(new_parents & self.females) > 1:
            return False
        self.parents[parent_name].add(child_name)
        self.children[child_name].add(parent_name)
        if len(new_parents) == 2:
            for parent in new_parents:
                if self.is_male(parent):
                    if not self.female(next(iter(new_parents - {parent}))):
                        return False
                elif self.is_female(parent):
                    if not self.male(next(iter(new_parents - {parent}))):
                        return False
            if len(new_parents & (self.males | self.females)) == 0:
                new_parents = list(new_parents)
                for (try_father, try_mother) in [new_parents, new_parents[::-1]]:
                    safe_males_copy, safe_females_copy = self.males.copy(), self.females.copy()
                    conflict_assign_gender = not self.male(try_father) or not self.female(try_mother)
                    self.males, self.females = safe_males_copy, safe_females_copy
                    if conflict_assign_gender:
                        return False
        return True
    def get_children_of(self, name):
        return sorted(self.parents[name])
    def get_parents_of(self, name):
        return sorted(self.children[name])

