class Node:

    def __init__(self, name):
        self.name = name
        self.is_dead = False
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.nodes = {kingName: Node(kingName)}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.nodes[parentName]
        child = Node(childName)
        parent.children.append(child)
        self.nodes[childName] = child

    def death(self, name: str) -> None:
        node = self.nodes[name]
        node.is_dead = True

    def getInheritanceOrder(self) -> List[str]:
        acc = []

        def getInheritanceOrderRecursive(node):
            if not node.is_dead:
                acc.append(node.name)
            for child in node.children:
                getInheritanceOrderRecursive(child)
        getInheritanceOrderRecursive(self.nodes[self.king_name])
        return acc
