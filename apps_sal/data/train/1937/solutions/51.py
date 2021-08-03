class P:
    def __init__(self, name):
        self.name = name
        self.child = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = P(kingName)
        self.d = {kingName: self.king}
        self.dead = set()

    def getnext(self, k):
        if k.name not in self.dead:
            yield k.name

        for c in k.child:
            yield from self.getnext(c)

    def birth(self, parentName: str, childName: str) -> None:
        child = P(childName)
        self.d[childName] = child
        self.d[parentName].child.append(child)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        return [*self.getnext(self.king)]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# [\"king\", \"andy\", \"matthew\", \"bob\", \"alex\", \"asha\", \"catherine\"]
# [\"king\", \"andy\", \"matthew\", \"alex\", \"asha\", \"catherine\"]
