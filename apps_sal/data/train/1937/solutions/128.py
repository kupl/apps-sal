class ThroneInheritance:
    class FamilyMember:
        def __init__(self, name: str):
            self.name = name
            self.children = []
            self.is_alive = True

        def newChild(self, name: str):
            child = ThroneInheritance.FamilyMember(name)
            self.children.append(child)
            return child

        def kill(self):
            self.is_alive = False

    king = None
    family = {}
    inheritenceOrder = []

    def __init__(self, kingName: str):
        self.king = self.FamilyMember(kingName)
        self.family[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        child = self.family[parentName].newChild(childName)
        self.family[childName] = child

    def death(self, name: str) -> None:
        self.family[name].kill()

    def buildInheritanceOrder(self, root: FamilyMember):
        if not root:
            return
        if root.is_alive:
            self.inheritenceOrder.append(root.name)
        for child in root.children:
            self.buildInheritanceOrder(child)
        return

    def getInheritanceOrder(self) -> List[str]:
        self.inheritenceOrder = []
        self.buildInheritanceOrder(self.king)
        return self.inheritenceOrder
