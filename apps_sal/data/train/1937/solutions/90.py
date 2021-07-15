from collections import defaultdict

class ThroneInheritance:
    # inheritance = []
    def __init__(self, kingName: str):
        self.family = defaultdict(list)
        self.king = kingName
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ans = []
        self.dfs(self.king)
        return self.ans
    
    def dfs(self, root):
        if root not in self.dead:
            self.ans.append(root)
        
        for child in self.family[root]:
            self.dfs(child)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

