class Node:
    def __init__(self, name):
        self.name = name
        self.children = list()
        self.alive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.map = defaultdict(Node)
        self.map[kingName] = Node(kingName)
        self.parent = defaultdict(str)
        self.king = kingName
        self.curOrder = [kingName]

    def birth(self, parentName: str, childName: str) -> None:
        self.map[childName] = Node(childName)
        self.map[parentName].children.append(childName)
        self.parent[childName] = parentName

    def death(self, name: str) -> None:
        self.map[name].alive = False
    # @lru_cache(None)

    def Successor(self, x):
        # print(self.map, self.parent)
        # print(x, self.curOrder)
        # self.curOrder += [x]
        flag = False
        for child in self.map[x].children:
            if child not in self.currSet:
                break
        else:
            flag = True
        if not self.map[x].children or flag:  # all of x's children are in curOrder:
            if x == self.king:
                return None
            else:
                return self.Successor(self.parent[x])
        else:
            # return x's oldest child who's not in curOrder
            for child in self.map[x].children:
                if child not in self.currSet:
                    return child
            return None

    def getInheritanceOrder(self) -> List[str]:
        self.curOrder = []
        self.currSet = set()
        name = self.king
        while name:
            self.curOrder.append(name)
            self.currSet.add(name)
            name = self.Successor(name)
        return [a for a in self.curOrder if self.map[a].alive]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
