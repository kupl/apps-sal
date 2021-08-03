class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.children = []
        self.siblings = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        
        self.root = TreeNode(kingName)
        self.mapping = collections.defaultdict()
        self.mapping[kingName] = self.root
        self.order = [kingName]
        self.parent = collections.defaultdict()
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        
        self.mapping[parentName].children.append(childName)
        self.mapping[childName] = TreeNode(childName)
        self.parent[childName] = parentName
        
    def death(self, name: str) -> None:
        
        self.dead.add(name)
        \"\"\"if name == 'king' or self.root.val == name:
            siblings = self.root.children[1:]
            print(name, 'name')
            self.root = self.mapping[self.root.children[0]]
            # move all sibilings to new root's children
            self.root.siblings += siblings
        else:
            parent_node = self.parent[name]
            idx = self.mapping[parent_node].children.index(name)
            # move death's parent to its grandparent
            for child in reversed(self.mapping[name].children):
                self.parent[child] = parent_node
                self.mapping[parent_node].children.insert(idx, child)
            self.mapping[self.parent[name]].children.remove(name)\"\"\"
        

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(node):
            res.append(node.val)
            for child in node.children:
                dfs(self.mapping[child])
        dfs(self.root)
        return [name for name in res if name not in self.dead]
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
