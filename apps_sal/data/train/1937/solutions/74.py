class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.childMap = dict([(kingName, [])])
        self.parentMap = dict([])
        self.grave = set([])

    def birth(self, parentName: str, childName: str) -> None:
        self.parentMap[childName] = parentName
        if parentName in self.childMap:
            self.childMap[parentName].append(childName)
        else:
            self.childMap[parentName] = [childName]

    def death(self, name: str) -> None:
        self.grave.add(name)

    def getInheritanceOrder(self) -> List[str]:
        curOrder = [self.kingName]
        curOrderSet = set(curOrder)
        n = self.successor(curOrder[-1], curOrder, curOrderSet)
        while n:
            curOrder.append(n)
            curOrderSet.add(n)
            n = self.successor(curOrder[-1], curOrder, curOrderSet)
        return [c for c in curOrder if c not in self.grave]

    def successor(self, x, curOrder, curOrderSet):
        if x in self.childMap:
            for c in self.childMap[x]:
                if c not in curOrderSet:
                    return c
        if x == self.kingName:
            return None
        return self.successor(self.parentMap[x], curOrder, curOrderSet)
