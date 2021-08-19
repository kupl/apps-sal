class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = collections.defaultdict(list)
        self.deaths = set()
        self.root = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def inorder(self, root, res):
        if root not in self.deaths:
            res.append(root)
        children = self.graph[root]
        for child in children:
            self.inorder(child, res)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        self.inorder(self.root, res)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
