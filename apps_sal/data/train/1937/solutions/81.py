class ThroneInheritance:

    def __init__(self, kingName: str):
        self.G = collections.defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.G[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def dfs(node, ans):
            if node not in self.dead:
                ans.append(node)
            for nei in self.G[node]:
                dfs(nei, ans)
        dfs(self.king, ans)
        return ans

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
