class Man:
    def __init__(self, name, father):
        self.name = name
        self.father = father
        self.children = []
        self.alive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.tree = Man(kingName, None)
        self.names = {kingName: self.tree}

    def birth(self, parentName: str, childName: str) -> None:
        father = self.names[parentName]
        man = Man(childName, father)
        father.children.append(man)
        self.names[childName] = man

    def death(self, name: str) -> None:
        self.names[name].alive = False

    def Succesor(self, man, curSet):
        if not man.children or all([c.name in curSet for c in man.children]):
            if man.father is None:
                return None
            else:
                return self.Succesor(man.father, curSet)
        else:
            for c in man.children:
                if c.name not in curSet:
                    return c
        return None

    def getInheritanceOrder(self) -> List[str]:
        curSet = set()
        curList = []
        if self.tree and self.tree.alive:
            king = self.tree.name
            curList.append(king)
            curSet.add(king)
        succesor = self.Succesor(self.tree, curSet)
        while succesor:
            if succesor.alive:
                curList.append(succesor.name)
            curSet.add(succesor.name)
            succesor = self.Succesor(succesor, curSet)
        return curList
