class TreeNode:
    def __init__(self, personName):
        self.name = personName
        self.children = []
        self.parent = None


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = TreeNode(kingName)
        self.dead = set()
        self.treeMap = {}
        self.treeMap[kingName] = self.king
        self.ret = []

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.treeMap[parentName]
        child = TreeNode(childName)

        self.treeMap[childName] = child
        child.parent = parent

        parent.children.append(child)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ret = []

        def helper(node):
            if node.name not in self.dead:
                self.ret.append(node.name)
            for i, child in enumerate(node.children):
                helper(node.children[i])

        helper(self.king)
        return self.ret
