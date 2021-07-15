class ThroneInheritance:
    
    def __init__(self, kingName: str):
        self.kingName = kingName
        self.inherit = {}
        self.inherit[kingName] = []
        self.dead = {kingName:False}
    
    def birth(self, parentName: str, childName: str) -> None:
        self.inherit[childName] = []
        self.inherit[parentName].append(childName)
        self.dead[childName] = False
        return
                
    def death(self, name: str) -> None:
        self.dead[name] = True


    def getInheritanceOrder(self) -> List[str]:
        return self.dfs(self.kingName)
        
    def dfs(self, name:str) -> List[str]:
        ret = []
        if not self.dead[name]:
            ret.append(name)
        for val in self.inherit[name]:
            ret += self.dfs(val)
        return ret
    
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

