class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isAlive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Node(kingName)
        self.dict = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        new_node = Node(childName)
        self.dict[parentName].children.append(new_node)
        self.dict[childName] = new_node

    def death(self, name: str) -> None:
        self.dict[name].isAlive = False

    def getInheritanceOrder(self) -> List[str]:
        ordering = []

        def preOrder(node):
            if node.isAlive:
                ordering.append(node.name)
            for c in node.children:
                preOrder(c)

        preOrder(self.king)
        return ordering
