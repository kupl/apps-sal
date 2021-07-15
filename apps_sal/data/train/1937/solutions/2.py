class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kName = kingName
        self.dead = set()
        self.cmap = {}

    def birth(self, parentName: str, childName: str) -> None:
        cmap = self.cmap
        if parentName not in self.cmap:
            cmap[parentName] = []
        cmap[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        # dfs
        res = []
        dfs(self.cmap, self.dead, self.kName, res)
        return res
    
def dfs(cmap, deaths, curr, res):
    if curr == None:
        return
    if curr not in deaths:
        res.append(curr)
    if curr in cmap:
        for child in cmap[curr]:
            dfs(cmap, deaths, child, res)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# inheritance -> king is first member
# recursive function Successor(x, curOrder) which gives person x and the inheritance order so far, returns who should be the nextg person after x in the order of inheritance.

