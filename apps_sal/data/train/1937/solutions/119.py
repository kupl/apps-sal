class ThroneInheritance:

    def __init__(self, kingName: str):
        self.result = defaultdict(list)
        self.king = kingName
        self.dead = set()
    
    def successor(self, x):
        if x not in self.dead:
            self.order.append(x)
        for i in self.result[x]:
            self.successor(i)

    def birth(self, parentName: str, childName: str) -> None:
        
        self.result[parentName].append(childName)


    def death(self, name: str) -> None:

        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        self.order = []
        name = self.king
        self.successor(name)
        return self.order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

