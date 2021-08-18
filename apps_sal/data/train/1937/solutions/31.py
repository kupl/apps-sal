class ThroneInheritance:

    def __init__(self, kingName: str):
        self.start = kingName
        self.deaths = {}
        self.relat = collections.defaultdict(list)
        self.relat[kingName] = []
        self.n = 1

    def birth(self, parentName: str, childName: str) -> None:
        self.relat[parentName].append(childName)
        self.n += 1

    def death(self, name: str) -> None:
        self.deaths[name] = True

    def getInheritanceOrder(self) -> List[str]:
        ret = []
        q = [self.start]
        while q:
            cur = q.pop()
            if cur not in self.deaths:
                ret.append(cur)
            for nxt in self.relat[cur][::-1]:
                q.append(nxt)
        return ret
