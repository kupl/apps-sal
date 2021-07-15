class ThroneInheritance:

    class Person:
        def __init__(self, name):
            self.name = name
            self.children = list()
            self.is_alive = True

    
    def __init__(self, kingName: str):
        self.root = ThroneInheritance.Person(kingName)
        self.tracker = {kingName: self.root}
        

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.tracker:
            return
        self.tracker[parentName].children.append(ThroneInheritance.Person(childName))
        self.tracker[childName] = self.tracker[parentName].children[-1]

    def death(self, name: str) -> None:
        self.tracker[name].is_alive = False
        

    def getInheritanceOrder(self) -> List[str]:
        
        res = list()
        
        def recursion(node):
            if node.is_alive:
                res.append(node.name)
            for child in node.children:
                recursion(child)
        recursion(self.root)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

