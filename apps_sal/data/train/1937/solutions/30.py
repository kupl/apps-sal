class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isAlive = True
        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Node(kingName)
        self.directory = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        parentnode = self.directory[parentName]
        childnode = Node(childName)
        parentnode.children.append(childnode)
        self.directory[childName] = childnode

    def death(self, name: str) -> None:
        self.directory[name].isAlive = False
        
    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(node):
            if not node: return
            if node.isAlive:
                ans.append(node.name)
            for child in node.children:
                dfs(child)
        dfs(self.king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

