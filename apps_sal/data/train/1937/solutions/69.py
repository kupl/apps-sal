from collections import defaultdict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead = defaultdict(bool)
        self.members = defaultdict(list)
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.members[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:
        inheritanceOrder = []

        def traverse(member):
            if not self.dead[member]:
                inheritanceOrder.append(member)
            for child in self.members[member]:
                traverse(child)

        traverse(self.king)
        return inheritanceOrder
