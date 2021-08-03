class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.parent = {}
        self.child = {}
        self.dead = set([])

    def birth(self, parentName: str, childName: str) -> None:
        self.addToHash(self.parent, childName, parentName)

        self.addToHash(self.child, parentName, childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def succesor(self, name, curOrder):
        if self.child.get(name):
            for c in self.child.get(name):
                if c not in curOrder:
                    return c
        if name == self.kingName:
            return None
        return self.succesor(self.parent[name][0], curOrder)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        cur = self.kingName
        inOrder = set([])
        while cur:
            if cur not in self.dead:
                res.append(cur)
            inOrder.add(cur)
            cur = self.succesor(cur, inOrder)
        return res

    def addToHash(self, hsh, key, value):
        if hsh.get(key):
            hsh.get(key).append(value)
        else:
            hsh[key] = [value]
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
