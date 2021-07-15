class ThroneInheritance:

    def __init__(self, kingName: str):
        self.k = kingName
        self.mp = defaultdict(list)
        self.d = set()

    def birth(self, p: str, c: str) -> None:
        self.mp[p].append(c)

    def death(self, name: str) -> None:
        self.d.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        stk = [self.k]
        while stk:
            x = stk.pop(0)
            if x not in self.d: ans.append(x)
            stk = self.mp[x] + stk
        return ans



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

