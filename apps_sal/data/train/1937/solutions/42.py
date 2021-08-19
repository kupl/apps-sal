import copy


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.parent = collections.defaultdict(list)
        self.children = collections.defaultdict(list)
        self.king = kingName
        self.deathList = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.parent[childName].append(parentName)
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deathList.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = [self.king]
        current = self.king
        c = copy.deepcopy(self.children)
        p = copy.copy(self.parent)

        def Successor(x, curOrder):
            if x not in c or len(c[x]) == 0:
                if x == self.king:
                    return None
                else:
                    return Successor(p[x][0], curOrder)
            newx = c[x].pop(0)
            curOrder.append(newx)
            return newx
        while current:
            current = Successor(current, order)
        if not self.deathList:
            return order
        else:
            neworder = []
            for name in order:
                if name not in self.deathList:
                    neworder.append(name)
            return neworder
