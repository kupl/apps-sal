
# ThroneInheritance(string kingName) Initializes an object of the ThroneInheritance class. The name of the king is given as part of the constructor.
# void birth(string parentName, string childName) Indicates that parentName gave birth to childName.
# void death(string name) Indicates the death of name. The death of the person doesn't affect the Successor function nor the current inheritance order. You can treat it as just marking the person as dead.
# string[] getInheritanceOrder() Returns a list representing the current order of inheritance excluding dead people.
from collections import OrderedDict


class Person:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.children = []
        self.parent = None
        self._successor = None

    @property
    def successor():
        if not self.children:
            return self.parent
        else:
            return self.children[0]


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Person(kingName)
        self.people = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.people[parentName]
        child = Person(childName)
        child.parent = parent
        self.people[childName] = child
        parent.children.append(child)

    def death(self, name: str) -> None:
        person = self.people[name]
        person.alive = False

    def successor(self, x, curOrder):
        curNames = set(curOrder)
        if not x.children or set([c.name for c in x.children]) <= curNames:
            if x.name == self.king.name:
                return None
            else:
                return self.successor(x.parent, curOrder)
        else:
            for c in x.children:
                if c.name not in curNames:
                    return c.name

    def inorder(self, t):
        res = [t.name]
        for c in t.children:
            res += self.inorder(c)
        return res

    def getInheritanceOrder(self) -> List[str]:
        return [name for name in self.inorder(self.king) if self.people[name].alive]

    def a():
        curOrder = [self.king.name]
        x = self.king
        while len(curOrder) < len(self.people):
            newsuc = self.successor(x, curOrder)
            x = self.people[newsuc]
            curOrder.append(newsuc)
        return [name for name in curOrder if self.people[name].alive]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
