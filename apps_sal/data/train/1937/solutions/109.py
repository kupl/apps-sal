class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.relation = {kingName: []}
        self.dead = {}

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.relation:
            self.relation[parentName].append(childName)
        else:
            self.relation[parentName] = [childName]

    def death(self, name: str) -> None:
        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:
        res = []
        self.dfs(self.kingName, res)
        return res

    def dfs(self, name, out):
        if name not in self.dead:
            out.append(name)
        if name not in self.relation:
            return
        for c in self.relation[name]:
            self.dfs(c, out)
        return


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
