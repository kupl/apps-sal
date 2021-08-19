class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = collections.defaultdict(list)
        self.root = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def dfs(self, name, arr):
        if name not in self.dead:
            arr.append(name)

        for nei in self.graph[name]:
            self.dfs(nei, arr)

        return arr

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        self.dfs(self.root, ans)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
