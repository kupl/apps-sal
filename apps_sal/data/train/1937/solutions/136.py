class Person:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.children = []

    def preOrder(self, output):
        if self.alive:
            output.append(self.name)
        for child in self.children:
            child.preOrder(output)


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Person(kingName)
        self.people = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = Person(childName)
        self.people[parentName].children.append(child)
        self.people[childName] = child

    def death(self, name: str) -> None:
        self.people[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        ret = []
        self.root.preOrder(ret)
        return ret
