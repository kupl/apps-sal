class node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isdead = False


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = node(kingName)
        self.m = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        p = self.m[parentName]
        c = node(childName)
        p.children.append(c)
        self.m[childName] = c

    def death(self, name: str) -> None:
        self.m[name].isdead = True

    def getInheritanceOrder(self) -> List[str]:
        cur = self.root
        res = []

        def helper(cur):
            if not cur.isdead:
                res.append(cur.name)
            for c in cur.children:
                helper(c)

        helper(cur)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
