class TreeNode:

    def __init__(self, name):
        self.name = name
        self.children = []
        self.alive = True


class ThroneInheritance:
    mapping = {}

    def __init__(self, kingName: str):
        self.mapping[kingName] = TreeNode(kingName)
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        c = TreeNode(childName)
        self.mapping[childName] = c
        self.mapping[parentName].children.append(c)

    def death(self, name: str) -> None:
        self.mapping[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        # Traverse the tree
        ret = []
        # print(\"?\")

        def dfs(node):
            # print(node.name)
            if node.alive:
                ret.append(node.name)
            for c in node.children:
                dfs(c)

        dfs(self.mapping[self.kingName])
        return ret


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
