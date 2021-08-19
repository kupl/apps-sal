class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.alive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.lookup = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        p = self.lookup[parentName]
        child = Node(childName)
        p.children.append(child)
        self.lookup[childName] = child

    def death(self, name: str) -> None:
        person = self.lookup[name]
        person.alive = False

    def getInheritanceOrder(self) -> List[str]:
        ret = []

        def dfs(node: Node):
            if node.alive:
                ret.append(node.name)
            for child in node.children:
                dfs(child)
        dfs(self.root)
        return ret


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
