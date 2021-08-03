class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.alive = {kingName: True}
        self.children = {kingName: []}
        self.parent = {kingName: None}

    def birth(self, parentName: str, childName: str) -> None:
        self.alive[childName] = True
        self.children[childName] = []
        self.children[parentName].append(childName)
        self.parent[childName] = parentName

    def death(self, name: str) -> None:
        self.alive[name] = False

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        if self.alive[self.king]:
            ans.append(self.king)
        cur = self.king
        index = [0]
        while cur:
            if len(self.children[cur]) > index[-1]:
                cur = self.children[cur][index[-1]]
                index[-1] += 1
                index.append(0)
                if self.alive[cur]:
                    ans.append(cur)
            else:
                cur = self.parent[cur]
                index.pop()
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
