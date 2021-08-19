class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.parents = collections.defaultdict(list)
        self.deads = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.parents[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []

        def dfs(name: str):
            if name not in self.deads:
                res.append(name)
            for child in self.parents[name]:
                dfs(child)
        dfs(self.king_name)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
