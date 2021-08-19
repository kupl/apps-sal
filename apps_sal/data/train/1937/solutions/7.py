# junge

class ThroneInheritance:
    root = ''
    children = {}
    dead = {}

    def __init__(self, kingName: str):
        self.root = kingName
        self.dead[self.root] = False
        self.children = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.dead[parentName] = False
        self.dead[childName] = False

    def death(self, name: str) -> None:
        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:
        res = []
        tosee = []
        tosee.append(self.root)
        while (len(tosee) != 0):
            cur = tosee[0]
            tosee.pop(0)

            if (self.dead[cur] == False):
                res.append(cur)

            for item in reversed(self.children[cur]):
                tosee.insert(0, item)

        return res
