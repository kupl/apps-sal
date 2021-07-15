class Node:
    def __init__(self, val):
        self.val = val
        self.child = []   # list of Nodes
        self.alive = True
        
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.dic = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.dic[parentName].child.append(child)
        self.dic[childName] = child

    def death(self, name: str) -> None:
        self.dic[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        # dfs
        res = []
        def dfs(node):
            if not node: return
            if node.alive: res.append(node.val)
            for n in node.child:
                dfs(n)
        dfs(self.root)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

