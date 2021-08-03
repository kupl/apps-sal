class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.descs = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.descs[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        stack = [self.king]

        ans = []

        while stack:
            heir = stack.pop()
            if heir not in self.dead:
                ans.append(heir)
            stack += self.descs[heir][::-1]

        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
