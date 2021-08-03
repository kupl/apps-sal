class ThroneInheritance:

    def __init__(self, kingName: str):
        # what structure to use
        # nested list, too hard to loop through?
        # list with tuples?
        # dictionary with each person being a key and part of an array value
        # keep dictionary of dead people?
        self.root = kingName
        self.inheritance = {kingName: []}
        self.dead = {}

    def birth(self, parentName: str, childName: str) -> None:
        # go through structure and add
        if parentName in self.inheritance:
            self.inheritance[parentName].append(childName)
        self.inheritance[childName] = []

    def death(self, name: str) -> None:
        # death doesn't affect successor function or current inheritance order
        # go through structure and delete
        self.dead[name] = 1

    def getInheritanceOrder(self) -> List[str]:
        # current order excluding dead people
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
