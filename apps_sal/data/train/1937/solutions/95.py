class ThroneInheritance:

    def __init__(self, kingName: str):
        self.nameBook = {}
        self.nameBook[kingName] = (kingName, [])
        self.king = self.nameBook[kingName]

        self.deathBook = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.nameBook:
            self.nameBook[childName] = (childName, [])
            self.nameBook[parentName][1].append(self.nameBook[childName])

    def death(self, name: str) -> None:

        self.deathBook.add(name)

    def getInheritanceOrder(self) -> List[str]:

        InheritOrder = []
        stack = [self.king]
        while stack:
            name, children = stack.pop()

            if name not in self.deathBook:
                InheritOrder.append(name)

            stack.extend(children[::-1])

        return InheritOrder


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
