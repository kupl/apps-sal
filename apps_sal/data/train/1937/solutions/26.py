class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.children = defaultdict(list)
        self.parent = {}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.parent[childName] = parentName
        
    def successor(self, name):
        for child in self.children[name]:
            if child not in self.order_set:
                self.order_set.add(child)
                self.curOrder.append(child)
                return child
        if name != self.kingName:
            return self.successor(self.parent[name])
        return None

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.curOrder = [self.kingName]
        self.order_set = set(self.curOrder)
        name = self.kingName
        while name:
            name = self.successor(name)
        return [name for name in self.curOrder if name not in self.dead]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

