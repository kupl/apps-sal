class Node(object):

    def __init__(self, name):
        self.name = name
        self.children = []
        self.isDead = False

    def addChild(self, child):
        self.children.append(child)


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.d = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.d[parentName].addChild(child)
        self.d[childName] = child

    def death(self, name: str) -> None:
        self.d[name].isDead = True

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(root):
            if not root:
                return
            if not root.isDead:
                order.append(root.name)
            for c in root.children:
                dfs(c)
        dfs(self.root)
        return order
