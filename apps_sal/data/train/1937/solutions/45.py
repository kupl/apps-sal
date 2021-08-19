class Family:

    def __init__(self, name):
        self.dead = False
        self.children = []
        self.name = name


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.family_map = {}
        member = Family(kingName)
        self.family_map[kingName] = member
        self.king = member

    def birth(self, parentName: str, childName: str) -> None:
        member = self.family_map[parentName]
        child = Family(childName)
        member.children.append(child)
        self.family_map[childName] = child

    def death(self, name: str) -> None:
        member = self.family_map[name]
        member.dead = True

    def getInheritanceOrder(self) -> List[str]:
        inheritance = []
        stack = [self.king]
        while len(stack):
            member = stack.pop()
            for child in member.children[::-1]:
                stack.append(child)
            if not member.dead:
                inheritance.append(member.name)
        return inheritance
