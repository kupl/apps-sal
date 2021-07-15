class ThroneInheritance:
    class Person:
        def __init__(self,name):
            self.name = name
            self.alive = True
    def __init__(self, kingName: str):
        self.tree = {}
        self.king = self.Person(kingName)
        self.name_map = {kingName:self.king}
        self.tree[self.king] = []
    
    def printTree(self):
        for p,v in self.tree.items():
            print(p.name + \" : \" ,end = \" \")
            for c in v:
                print(c.name, end = \"  \")
            print()
    
    def birth(self, parentName: str, childName: str) -> None:
        child = self.Person(childName)
        self.tree[self.name_map[parentName]].append(child)
        self.name_map[childName] = child
        self.tree[child] = []
        #self.printTree()
        

    def death(self, name: str) -> None:
        self.name_map[name].alive = False
        

    def getInheritanceOrder(self) -> List[str]:
        inheritance = []
        def rec(person):
            if person.alive:
                inheritance.append(person.name)
            for child in self.tree[person]:
                rec(child)
        rec(self.king)
        return inheritance
                
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
