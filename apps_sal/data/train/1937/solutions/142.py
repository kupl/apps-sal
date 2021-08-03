class Node:
    def __init__(self):
        self.name = None
        self.children = []
        self.parent = None
        self.isDead = False


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node()
        self.root.name = kingName
        self.lookup = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        curr = Node()
        curr.name = childName
        curr.parent = parentName

        self.lookup[parentName].children.append(curr)
        self.lookup[childName] = curr

    def death(self, name: str) -> None:
        self.lookup[name].isDead = True

    def getInheritanceOrder(self) -> List[str]:
        return self.dfs(self.root)

    def dfs(self, node):
        if node.isDead:
            result = []
        else:
            result = [node.name]
        for c in node.children:
            result += self.dfs(c)

        return result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
