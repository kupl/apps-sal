from collections import OrderedDict, defaultdict

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.parent2son = {}
        self.parent2son[kingName] = OrderedDict()
        self.son2parent = {}
        self.deadset = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.son2parent[childName] = parentName
        if parentName not in self.parent2son:
            self.parent2son[parentName] = OrderedDict()
        self.parent2son[parentName][childName] = 0
        

    def death(self, name: str) -> None:
        self.deadset.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        stack = [self.kingName]
        while stack:
            name = stack.pop()
            if name in self.parent2son:
                next = []
                for son in self.parent2son[name]:
                    next.insert(0, son)
                stack = stack + next
            if name not in self.deadset:
                order.append(name)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

