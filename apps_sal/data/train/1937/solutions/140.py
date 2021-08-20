class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.inh = {kingName: (None, True, [])}

    def birth(self, parentName: str, childName: str) -> None:
        self.inh[parentName][-1].append(childName)
        self.inh[childName] = (parentName, True, [])

    def death(self, name: str) -> None:
        (p, _, ch) = self.inh[name]
        self.inh[name] = (p, False, ch)

    def getInheritanceOrder(self) -> List[str]:
        order = [self.king]
        s = set(order)

        def fs(x):
            (p, a, ch) = self.inh[x]
            for c in ch:
                order.append(c)
                s.add(c)
                fs(c)
        fs(self.king)
        return [o for o in order if self.inh[o][1]]
