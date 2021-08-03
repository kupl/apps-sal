class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.pc = defaultdict(list)
        self.deathset = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.pc[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deathset.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        self.recur(self.king, ans)
        return ans

    def recur(self, name: str, ans: List[str]) -> None:
        if name not in self.deathset:
            ans.append(name)
        for child in self.pc[name]:
            self.recur(child, ans)

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
