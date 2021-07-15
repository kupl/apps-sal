class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        
    def add(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
    
    def die(self):
        index = self.parent.children.index(self)
        #print(index, self.parent.children)
        self.parent.children[index:index] = self.children
        self.parent.children.remove(self) # remove from parents children
        for child in self.children:
            child.parent = self.parent
        self.parent = None


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.nodes = {}
        root = Node(\"\")
        self.nodes[\"\"] = root
        self.birth(\"\", kingName)
        
    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.nodes[childName] = child
        parent = self.nodes[parentName]
        parent.add(child)

    def death(self, name: str) -> None:
        self.nodes[name].die()
        del self.nodes[name]

    def getInheritanceOrder(self) -> List[str]:
        path = []
        def dfs(node):
            path.append(node.name)
            for child in node.children:
                dfs(child)
        dfs(self.nodes[\"\"])
        return path[1:]
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
