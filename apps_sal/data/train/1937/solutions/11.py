class ThroneInheritance:
    
    allNames={}

    def __init__(self, kingName: str):
        # order=[kingName]
        # familyTree=Tree(kingName)
        self.name=kingName
        self.alive=True
        self.children=[]
        self.allNames[kingName]=self

    def birth(self, parentName: str, childName: str) -> None:
        self.allNames[parentName].children+=[ThroneInheritance(childName)]          

    def death(self, name: str) -> None:
        self.allNames[name].alive=False 
    
    def getInheritanceOrder(self) -> List[str]:
        answ=[]
        if self.alive: answ+=[self.name]    
        for child in self.children:
            answ+=child.getInheritanceOrder()
        return answ



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

