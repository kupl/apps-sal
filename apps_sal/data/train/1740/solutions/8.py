from collections import defaultdict, deque
from copy import deepcopy

class Member:
    def __init__(self, name, gender=''):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return self.name

class family:
    def __init__(self):
        self.children = defaultdict(list)
        self.member_objects = []

    def get_member(self, name):
        member = next((i for i in self.member_objects if i.name == name), None)
        if member is None:
            self.member_objects.append(Member(name))
            return self.member_objects[-1]
        return member

    def male(self, name):
        member = self.get_member(name)
        if member.gender == 'female' : return False
        member.gender = 'male'
        self.set_rest_of_things()
        return True

    def is_male(self, name):
        gdr = self.get_member(name).gender
        return bool(gdr) and gdr == 'male'

    def female(self, name):
        member = self.get_member(name)
        if member.gender == 'male' : return False
        member.gender = 'female'
        self.set_rest_of_things()
        return True

    def is_female(self, name):
        gdr = self.get_member(name).gender
        return bool(gdr) and gdr == 'female'

    def is_cycle(self, child, parent):
        copy = defaultdict(list, {i.name: [k.name for k in j] for i, j in self.children.items()})
        copy[child.name].append(parent.name)
        Q = deque([[parent.name, []]])
        while Q:
            node, path = Q.popleft()
            path.append(node)
            for neighbour in copy[node]:
                if neighbour not in path : Q.append([neighbour, path[:]])
                elif neighbour == parent.name : return True
        return False

    def is_consistent(self, child, parent):
        if self.is_cycle(child,parent) : return True
        temp = Member('GG')
        self.children[child].append(temp)
        copy = deepcopy(self.children)
        self.children[child].remove(temp)
        nodes = set([i for i in copy] + [j for i in copy.values() for j in i])
        for i in nodes : i.gender = ''
        prt = next((i for i in nodes if i.name == parent.name), None)
        if not prt : return False
        prt.gender = 'male'   
        k = self.set_rest_of_things(copy,prt)
        return 'malefemale' in k or 'femalemale' in k

    def set_parent_of(self, child, parent):
        child, parent = self.get_member(child), self.get_member(parent)
        if parent in self.children[child] or parent in self.children[child] : return True
        if child == parent or len(self.children[child]) == 2 or \
           parent.gender and self.children[child] and self.children[child][0].gender == parent.gender or self.is_consistent(child, parent) : return False

        self.children[child].append(parent)
        self.set_rest_of_things()
        return True

    def get_children_of(self, name):
        return sorted([i.name for i, j in self.children.items() if name in [k.name for k in j]])

    def get_parents_of(self, name):
        return sorted(next(([k.name for k in j] for i, j in self.children.items() if i.name == name), []))

    def set_rest_of_things(self,cpy='',prt=''):
        cpy = self.children if not cpy else cpy
        d, i, keys, genders = {'male': 'female', 'female': 'male'}, 0, list(cpy.keys()), defaultdict(str)
        while i < len(keys): 
            parents = cpy[keys[i]]
            if len(parents) > 1:
                a, b = parents
                if (a.gender, b.gender).count('') == 1: 
                    b.gender = d.get(a.gender, b.gender)
                    a.gender = d.get(b.gender, a.gender)
                    genders[a.name] = a.gender 
                    genders[b.name] = b.gender
                    i = -1                                              
            i += 1
        return genders[prt.name] + genders['GG'] if prt else ''
