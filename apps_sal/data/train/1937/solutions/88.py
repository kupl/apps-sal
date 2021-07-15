class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.personDict = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.personDict[parentName].append(childName)        

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ans=[]
        self.dfs(self.kingName)
        return self.ans
        
    def dfs(self,name: str):
        if name not in self.dead:
            self.ans.append(name)
        for childName in self.personDict[name]:
            self.dfs(childName)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

