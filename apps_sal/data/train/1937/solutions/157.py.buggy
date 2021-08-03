class Person:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.children = []

    def __str__(self):
        parts = []
        parts.append(self.name)
        if self.alive == False:
            parts.append(\"dead\")
        parts.append(\"(\")
        for child in self.children:
            parts.append(child.name)
        parts.append(\")\")
        return \" \".join(parts)

class ThroneInheritance:

    def createPerson(self, name):
        p = Person(name)
        self.lookup[name] = p
        return p
    
    def __init__(self, kingName: str):
        self.lookup = dict()
        self.king = self.createPerson(kingName)
        
        print(self.lookup)
        print(self.king)

    def birth(self, parentName: str, childName: str) -> None:
        p = self.lookup[parentName]
        child = self.createPerson(childName)
        p.children.append(child)
        print(p)

    def death(self, name: str) -> None:
        self.lookup[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def doit(p):
            if p != None:
                if p.alive:
                    order.append(p.name)
                for c in p.children:
                    doit(c)
        doit(self.king)
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
