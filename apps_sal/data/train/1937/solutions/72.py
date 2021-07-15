class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.alive = True
    def dfs(self):
        res = []
        if self.alive:
            res.append(self.name)
        for child in self.children:
            res.extend(child.dfs())
        return res

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Person(kingName)
        self.mapping = {}
        self.mapping[kingName] = self.root

    def birth(self, parentName: str, childName: str) -> None:
        newOne = Person(childName)
        parent = self.mapping[parentName]
        self.mapping[childName] = newOne
        parent.children.append(newOne)

    def death(self, name: str) -> None:
        self.mapping[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        return self.root.dfs()


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

