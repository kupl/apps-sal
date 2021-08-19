class ThroneInheritance:

    def __init__(self, kingName: str):
        self.lineageTree = [kingName, []]
        self.lineageLocs = {kingName: self.lineageTree}
        self.deaths = set([])

    def birth(self, parentName: str, childName: str) -> None:
        parentLoc = self.lineageLocs[parentName]
        parentLoc[1].append([childName, []])
        self.lineageLocs[childName] = parentLoc[1][-1]

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:

        def doit(node, deaths):
            if node == []:
                return []
            res = []
            if node[0] not in deaths:
                res.append(node[0])
            for childNode in node[1]:
                res = res + doit(childNode, deaths)
            return res
        return doit(self.lineageTree, self.deaths)
