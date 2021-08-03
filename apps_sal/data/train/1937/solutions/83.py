class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = collections.defaultdict(lambda: [])
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def dfs(root):
            if not root:
                return
            if root not in self.dead:
                ans.append(root)
            for child in self.graph[root]:
                dfs(child)
        dfs(self.king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
