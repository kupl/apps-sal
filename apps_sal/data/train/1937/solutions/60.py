class ThroneInheritance:

    def __init__(self, kingName: str):
        self.alive = {kingName: True}
        self.children = {kingName: []}
        self.order = [kingName]
        self.kingName = kingName
        self.placed = set([kingName])
        self.parent = {}

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.children[childName] = []
        self.parent[childName] = parentName
        self.alive[childName] = True

    def death(self, name: str) -> None:
        self.alive[name] = False

    def getInheritanceOrder(self) -> List[str]:
        curr = self.kingName
        while True:
            curr = self.succ(curr)
            if curr is None:
                break
            self.order.append(curr)
            self.placed.add(curr)
        ret = [o for o in self.order if self.alive[o]]
        self.placed = set([self.kingName])
        self.order = [self.kingName]
        return ret
        
    def succ(self, x) -> str:
        if not self.children[x] or all([c in self.placed for c in self.children[x]]):
            if x == self.kingName:
                return None
            return self.succ(self.parent[x])
        for c in self.children[x]:
            if c not in self.placed:
                return c


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

