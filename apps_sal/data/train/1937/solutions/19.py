class Tree:
    def __init__(self, name):
        self.val = name
        self.descents = []
        
        
class ThroneInheritance:
    
    def __init__(self, kingName: str):
        self.dic={}  # name:实体
        self.dead = set()
        self.kingNode=Tree(kingName)
        self.dic[kingName] = self.kingNode
        
    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.dic:
            node = Tree(parentName)
            self.dic[parentName] = node
        childNode = Tree(childName)
        self.dic[childName] = childNode
        self.dic[parentName].descents.append( childNode )
        
    def death(self, name: str) -> None:
        self.dead.add(self.dic[name])

        
        
    def output(self,root):
        
        if root not in self.dead:
            self.ans.append(root.val)
        for child in root.descents:
            self.output(child)
        
        
        
    def getInheritanceOrder(self) -> List[str]:
        self.ans=[]
        self.output(self.kingNode)
        return self.ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

