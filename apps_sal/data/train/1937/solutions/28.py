class ThroneInheritance:

    def __init__(self, kingName: str):
        self.d = defaultdict(list)
        self.deads = set()
        self.k = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.d[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        arr = []
        def getChildren(name):
            if name not in self.deads:
                arr.append(name)
            for child in self.d[name]:
                getChildren(child)
        
        getChildren(self.k)
        return arr
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

