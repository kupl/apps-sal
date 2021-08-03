class Member:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.nextChild = None
        self.nextSibling = None


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.members = {}
        self.lastChild = {}

        self.king = Member(kingName)
        self.members[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.members[parentName]

        child = Member(childName)
        self.members[childName] = child

        if parentName in self.lastChild:
            member = self.lastChild[parentName]
            member.nextSibling = child
        else:
            parent.nextChild = child
        self.lastChild[parentName] = child

    def death(self, name: str) -> None:
        self.members[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        inheritanceOrder = []

        def traverseInOrder(member):
            if member is None:
                return

            if member.alive:
                inheritanceOrder.append(member.name)
            traverseInOrder(member.nextChild)
            traverseInOrder(member.nextSibling)

        traverseInOrder(self.king)
        return inheritanceOrder


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
