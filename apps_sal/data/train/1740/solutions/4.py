class Person:
    def __init__(self, name):
        self.name = name
        self.parents = set()
        self.children = set()
        self.gender = 0
    def is_ancestor_of(self, person):
        ancestors = set()
        generation = set([person])
        while len(generation):
            ancestors = ancestors.union(generation)
            next_generation = set()
            for ancestor in generation:
                if self in ancestor.parents:
                    return True
                next_generation = next_generation.union(ancestor.parents)
            generation = next_generation

class Transaction(list):
    def __init__(self):
        list.__init__(self)
    def start(self):
        self.append(lambda: None)
    def end(self, commit):
        if commit:
            self.log(self.pop())
        else:
            self.pop()()
        return commit
    def log(self, undo):
        if not len(self):
            self.start()
        self.append((lambda rest: lambda: (undo(), rest()))(self.pop()))

class Family:
    def __init__(self):
        self.people = {}
        self.transaction = Transaction()
    def _member(self, name):
        if not name in self.people:
            self.people[name] = Person(name)
        return self.people[name]
    def set_parent_of(self, child, parent):
        if child == parent:
            return False
        child = self._member(child)
        parent = self._member(parent)
        if parent in child.parents:
            return True
        self.transaction.start()
        child.parents.add(parent)
        parent.children.add(child)
        self.transaction.log(lambda: (child.parents.remove(parent), parent.children.remove(child)))
        success = not child.is_ancestor_of(parent) and self._rule_parents(child)
        self.transaction.end(success)
        return success
    def male(self, person):
        return self._set_gender_of(self._member(person), 1)
    def is_male(self, person):
        return self._member(person).gender == 1
    def female(self, person):
        return self._set_gender_of(self._member(person), -1)
    def is_female(self, person):
        return self._member(person).gender == -1
    def get_children_of(self, person):
        return sorted([p.name for p in self._member(person).children])
    def get_parents_of(self, person):
        return sorted([p.name for p in self._member(person).parents])
    def _rule_parents(self, child):
        if len(child.parents) != 2:
            return len(child.parents) < 2
        female = [person for person in child.parents if person.gender == -1]
        male = [person for person in child.parents if person.gender == 1]
        undetermined = [person for person in child.parents if person.gender == 0]
        if not len(undetermined):
            return len(child.parents) < 2 or len(male) | len(female) == 1
        if len(undetermined) < len(child.parents):
            return self._set_gender_of(undetermined[0], len(female)-len(male))
        # Two possibilities: try one just to see if it leads to a gender-inconsistency
        self.transaction.start()
        success = self._set_gender_of(undetermined[0], 1)
        self.transaction.end(0)
        return success
    def _set_gender_of(self, person, gender):
        if person.gender == gender:
            return True
        if person.gender == -gender:
            return False
        person.gender = gender
        self.transaction.log(lambda: setattr(person, "gender", 0))
        return all(self._rule_parents(child) for child in person.children)

