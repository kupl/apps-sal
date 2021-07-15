class Tree: 
    def __init__(self, name, state = \"live\"): 
        self.children = []
        self.name = name
        self.state = state
   
    
class ThroneInheritance:
    
    king = \"\"
    root = None
    order = {}
    def __init__(self, kingName: str):
        self.king = kingName
        self.root = Tree(kingName)
        self.order[kingName] = self.root

    def birth(self, parentName: str, childName: str) -> None:
        node = Tree(childName)
        
        if parentName == self.king: 
            self.root.children.append(node)
        else: 
            self.order[parentName].children.append(node)
            
        self.order[childName] = node

    def death(self, name: str) -> None:
        self.order[name].state = \"dead\"

    def getInheritanceOrder(self) -> List[str]:
        return self.preorder(self.root)
            
    def preorder(self, root): 
        if root is None: return []
        
        sk, out = [root, ], []
    
        while sk: 
            root = sk.pop()
            if root.state == \"live\": 
                out.append(root.name)
            sk.extend(root.children[::-1])
            
        return out

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
