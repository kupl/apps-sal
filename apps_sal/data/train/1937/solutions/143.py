class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.deathed = set()
        self.hmap = {kingName: []}

    def birth(self, parentName: str, childName: str) -> None:
        self.hmap[parentName].append(childName)
        self.hmap[childName] = []

    def death(self, name: str) -> None:
        self.deathed.add(name)

    def getInheritanceOrder(self) -> List[str]:

        def dfs(node):
            # nonlocal ans
            for st in self.hmap[node]:
                if st not in self.deathed:
                    ans.append(st)
                dfs(st)
        ans = [self.root] if self.root not in self.deathed else []
        dfs(self.root)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
