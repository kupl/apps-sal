class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.inh = {kingName: (None, True, [])}

    def birth(self, parentName: str, childName: str) -> None:
        self.inh[parentName][-1].append(childName)
        self.inh[childName] = (parentName, True, [])

    def death(self, name: str) -> None:
        p, _, ch = self.inh[name]
        self.inh[name] = (p, False, ch)

    def getInheritanceOrder(self) -> List[str]:
        # print(self.inh)
        order = [self.king]
        s = set(order)
        # inord = {k: cc[::-1] for k, (pp, _, cc) in self.inh.items()}
        def fs(x):
            p, a, ch = self.inh[x]
            # if not inord[x]: #  no children or all of x's children are in curOrder:
            #     if x != self.king:
            #         fs(p)
            # else:
            for c in ch:
                order.append(c)
                s.add(c)
                # inord[x].pop()
                fs(c)
        fs(self.king)
        return [o for o in order if self.inh[o][1]]


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

