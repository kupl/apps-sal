
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead = {}
        self.mp = {}
        self.mp[kingName] = []
        
    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.mp:
            self.mp[parentName] = []
        self.mp[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(self, res, node):
            if node not in self.dead:
                res.append(node)
            if node not in self.mp:
                return
            for child in self.mp[node]:
                dfs(self, res, child)
        dfs(self, res, self.king)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

