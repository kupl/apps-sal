class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.hm = {kingName: self.root}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        pnode = self.hm[parentName]
        cNode = Node(childName)
        self.hm[childName] = cNode
        pnode.children.append(cNode)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []

        def dfs(node):
            if node.name not in self.dead:
                res.append(node.name)
            for child in node.children:
                dfs(child)

        dfs(self.root)
        return res
