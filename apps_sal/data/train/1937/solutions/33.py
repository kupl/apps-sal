class ThroneInheritance:

    def __init__(self, kingName: str):
        self.died = set()
        self.hmap = defaultdict(lambda : list())
        

    def birth(self, parentName: str, childName: str) -> None:
        self.hmap[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.died.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        res = list()
        q = [\"king\"]
        
        while q:
            name = q.pop()
            
            if name not in self.died:
                res.append(name)
                
            for child in self.hmap[name][::-1]:
                q.append(child)
                
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
