class Person:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[\"Person\"] = list()
        self.alive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.head: Person = Person(kingName)
        self.data = {kingName: self.head}
        self.memo = (0, [])
        

    def birth(self, parentName: str, childName: str) -> None:
        
        current = Person(childName)
        self.data[parentName].children.append(current)
        self.data[childName] = current


    def death(self, name: str) -> None:
        
        self.data[name].alive = False
        

    def getInheritanceOrder(self) -> List[str]:
        
        horizon, seen, out = [(self.head, iter(self.head.children))], set(), []
        while horizon:
            current, children_iter = horizon[-1]
            if current not in seen:
                seen.add(current)
                if current.alive:
                    out.append(current.name)
            try:
                child = next(children_iter)
            except StopIteration:
                horizon.pop()
                continue
            else:
                horizon.append((child, iter(child.children)))
                
        return out
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
