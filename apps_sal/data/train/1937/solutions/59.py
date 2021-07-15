class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):        
        self.root = Node(kingName)
        self.n2n = {kingName:self.root}
        self.dead = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        node = Node(childName)
        self.n2n[parentName].children.append(node)
        self.n2n[childName] = node

    def death(self, name: str) -> None:
        self.dead.add(name)        

    def getInheritanceOrder(self) -> List[str]:
        root = self.root
        res = []
        def dfs(root) -> None:
            if root.name not in self.dead:
                res.append(root.name)
            for child in root.children:
                dfs(child)
        dfs(root)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

