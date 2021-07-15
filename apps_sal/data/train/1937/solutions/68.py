from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.family = defaultdict(list)
        self.dead = set()
        self.parent = dict()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)
        self.parent[childName] = parentName
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        order = [self.kingName]
        
        self.getInheritanceOrderFor(self.kingName, order)
        
        return [x for x in order if x not in self.dead]
        
    def getInheritanceOrderFor(self, name, order):
        for child in self.family[name]:
            order.append(child)
            self.getInheritanceOrderFor(child, order)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

