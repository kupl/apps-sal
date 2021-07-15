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
        self.node = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.node[parentName].addChild(child)
        self.node[childName] = child
            
    def death(self, name: str) -> None:
        self.node[name].isDead = True

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
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

