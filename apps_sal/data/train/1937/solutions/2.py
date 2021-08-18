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
