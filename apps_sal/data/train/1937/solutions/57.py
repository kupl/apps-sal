class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.inheritance = {kingName: []}
        self.dead = {}

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.inheritance:
            self.inheritance[parentName].append(childName)
        self.inheritance[childName] = []

    def death(self, name: str) -> None:
        self.dead[name] = 1

    def getInheritanceOrder(self) -> List[str]:
        arr = []
        arr2 = []
        self.helper(self.root, arr)
        for person in arr:
            if person in self.dead:
                pass
            else:
                arr2.append(person)
        return arr2

    def helper(self, parent, arr):
        if len(self.inheritance[parent]) == 0:
            arr.append(parent)
            return
        arr.append(parent)
        for child in self.inheritance[parent]:
            self.helper(child, arr)
