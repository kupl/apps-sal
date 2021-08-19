class Member:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.nextChild = None
        self.nextSibling = None


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.members = {}
        self.king = Member(kingName)
        self.members[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.members[parentName]
        child = Member(childName)
        self.members[childName] = child
        if parent.nextChild is None:
            parent.nextChild = child
            return
        member = parent.nextChild
        while member.nextSibling:
            member = member.nextSibling
        member.nextSibling = child

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
