class TreeNode:

    def __init__(self, val):
        self.val = val
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):

        self.root = TreeNode(kingName)
        self.mapping = collections.defaultdict()
        self.mapping[kingName] = self.root
        self.parent = collections.defaultdict()
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:

        self.mapping[parentName].children.append(childName)
        self.mapping[childName] = TreeNode(childName)
        self.parent[childName] = parentName

    def death(self, name: str) -> None:

        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []

        def dfs(node):
            res.append(node.val)
            for child in node.children:
                dfs(self.mapping[child])
        dfs(self.root)
        return [name for name in res if name not in self.dead]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
