class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.tree = collections.defaultdict(list)
        self.tree[kingName] = []
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(name):
            res.append(name)
            for child in self.tree[name]:
                dfs(child)
        dfs(self.king)
        return [name for name in res if name not in self.dead]
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

