class ThroneInheritance:

    def __init__(self, kingName: str):
        self.g = collections.defaultdict(list)
        self.rg = {}
        self.ROOT = kingName
        self.deathS = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.g[parentName].append(childName)
        self.rg[childName] = parentName

    def death(self, name: str) -> None:
        self.deathS.add(name)

    def getInheritanceOrder(self) -> List[str]:

        def succeed(x, currentOrder):
            if x:
                if len(self.g[x]) == 0 or all(i in currentOrder for i in self.g[x]):
                    if x == self.ROOT:
                        return None
                    else:
                        return succeed(self.rg[x], currentOrder)
                else:
                    for i in self.g[x]:
                        if i not in currentOrder:
                            return i
            return None

        st = [self.ROOT]
        currentOrder = set()
        while st[-1] not in currentOrder:
            c = st[-1]
            currentOrder.add(c)
            nn = succeed(c, currentOrder)
            if nn:
                st.append(nn)
        res = [i for i in st if i not in self.deathS]
        return res
