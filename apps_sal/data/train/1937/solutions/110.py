# 1600
class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.alive = True

    def birth(self, name):
        self.children.append(Person(name))
        return self.children[-1]


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = Person(kingName)
        self.dic = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.dic[parentName]
        child = parent.birth(childName)
        self.dic[childName] = child

    def death(self, name: str) -> None:
        self.dic[name].alive = False

    def getInheritanceOrder(self) -> 'List[str]':
        res = []
        stack = [self.king]
        while stack:
            p = stack.pop()
            if p.alive:
                res.append(p.name)
            for child in p.children[::-1]:
                stack.append(child)
        return res
