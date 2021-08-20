class people:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.dic = {}
        self.dic[kingName] = people(kingName)

    def birth(self, parentName: str, childName: str) -> None:
        child = people(childName)
        self.dic[childName] = child
        self.dic[parentName].children.append(child)

    def death(self, name: str) -> None:
        self.dic[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        order = self.dfs(self.dic[self.kingName])
        res = []
        for o in order:
            if o.alive is True:
                res.append(o.name)
        return res

    def dfs(self, cur):
        res = []
        res.append(cur)
        for child in cur.children:
            temp = self.dfs(child)
            res += temp
        return res
