class Person:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[\"Person\"] = list()
        self.alive = True
        self.next = self.prev = None


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.head: Person = Person(kingName)
        self.data = {kingName: self.head}
        

    def birth(self, parentName: str, childName: str) -> None:
        
        current = Person(childName)
        prev = self.data[parentName]
        while prev.children:
            prev = prev.children[-1]
            
        if prev.next is not None:
            next = prev.next
            prev.next, current.prev = current, prev
            current.next, next.prev = next, current
        else:
            prev.next, current.prev = current, prev
                
        self.data[parentName].children.append(current)
        self.data[childName] = current


    def death(self, name: str) -> None:
        
        self.data[name].alive = False
        

    def getInheritanceOrder(self) -> List[str]:
        
        current, out = self.head, []
        while current is not None:
            if current.alive:
                out.append(current.name)
            current = current.next
        return out
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
