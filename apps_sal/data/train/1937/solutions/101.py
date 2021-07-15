class Person:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[\"Person\"] = list()
        self.alive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.head: Person = Person(kingName)
        self.data = {kingName: self.head}
        

    def birth(self, parentName: str, childName: str) -> None:
        
        current = Person(childName)
        self.data[parentName].children.append(current)
        self.data[childName] = current


    def death(self, name: str) -> None:
        
        self.data[name].alive = False
        

    def getInheritanceOrder(self) -> List[str]:
        
        seen, out = set(), []
        
        def _helper(node):
            if node not in seen:
                seen.add(node)
                if node.alive:
                    out.append(node.name)
                    
            for child in node.children:
                _helper(child)
                
        _helper(self.head)
        return out
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
