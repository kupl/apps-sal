class Person:

    def __init__(self):
        self.sex = None
        self.children = []
        self.parents = []

class Family:

    def __init__(self):
        self.members = dict()

    def get_parents_gap(self, first, second):
        if first not in self.members or second not in self.members:
            return None
        kids = self.members[first].children[:]
        parents, step = [first], 0
        while kids:
            parents_size = len(parents)
            for kid in kids:
                parents.extend([p for p in self.members[kid].parents if p not in parents])
            del parents[:parents_size]
            if second in parents:
                return step
            kids_size = len(kids)
            for parent in parents:
                kids.extend([k for k in self.members[parent].children if k not in kids])
            del kids[:kids_size]
            step += 1
        return None

    def get_parent_sex(self, name):
        kids = self.members.get(name, Person()).children[:]
        parents, kid_step = [name], 0
        while kids:
            parents_size = len(parents)
            for kid in kids:
                parents.extend([p for p in self.members[kid].parents if p not in parents])
            del parents[:parents_size]
            kids_size = len(kids)
            for parent in parents:
                person = self.members[parent]
                if person.sex == 'male':
                    return 'male' if kid_step%2 else 'female'
                elif person.sex == 'female':
                    return 'female' if kid_step%2 else 'male'
                kids.extend([k for k in person.children if k not in kids])
            del kids[:kids_size]
            kid_step += 1
        return None
        
    def male(self, name):
        person = self.members.get(name, Person())
        if person.sex == 'female':
            return False
        elif person.sex is None:
            if self.get_parent_sex(name) == 'female':
                return False
            person.sex = 'male'
            self.members[name] = person
        return True
    
    def is_male(self, name):
        if self.members.get(name, Person()).sex == 'male':
            return True
        return self.get_parent_sex(name) == 'male'
    
    def female(self, name):
        person = self.members.get(name, Person())
        if person.sex == 'male':
            return False
        elif person.sex is None:
            if self.get_parent_sex(name) == 'male':
                return False
            person.sex = 'female'
            self.members[name] = person
        return True

    def is_female(self, name):
        if self.members.get(name, Person()).sex == 'female':
            return True
        return self.get_parent_sex(name) == 'female'
    
    def set_parent_of(self, child_name, parent_name):
        if  child_name == parent_name:
            return False
        child = self.members.get(child_name, Person())
        parent = self.members.get(parent_name, Person())
        if child_name in parent.children:
            return True
        elif len(child.parents)==2:
            return False
        kids = child.children[:]
        while kids:
            if parent_name in kids:
                return False
            for _ in range(len(kids)):
                kids.extend(self.members[kids.pop(0)].children)
        fp_sex = None
        if child.parents:
            fp_sex = self.members[child.parents[0]].sex
            if fp_sex is None:
                fp_sex = self.get_parent_sex(child.parents[0])
        sp_sex = self.get_parent_sex(parent_name) if parent.sex is None else parent.sex
        if fp_sex==sp_sex and fp_sex is not None:
            return False
        if (fp_sex is None and sp_sex is None and
            child.parents and parent_name in self.members):
            gap = self.get_parents_gap(child.parents[0], parent_name)
            if gap is not None and gap%2:
                return False
        child.parents.append(parent_name)
        parent.children.append(child_name)
        self.members[child_name] = child
        self.members[parent_name] = parent
        return True
    
    def get_children_of(self, name):
        return sorted(self.members.get(name, Person()).children)
    
    def get_parents_of(self, name):
        return sorted(self.members.get(name, Person()).parents)

