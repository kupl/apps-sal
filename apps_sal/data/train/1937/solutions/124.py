class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def addChild(self, child):
        self.children.append(child)


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.node = {kingName: self.root}
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.node[parentName]
        child = Node(childName, parent)
        parent.addChild(child)
        self.node[childName] = child

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(root):
            if not root:
                return
            if root.name not in self.deaths:
                order.append(root.name)
            for c in root.children:
                dfs(c)
        dfs(self.root)
        return order
