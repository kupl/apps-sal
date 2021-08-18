class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.family = defaultdict(list)
        self.deadName = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deadName.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []

        def dfs(name):
            if name not in self.deadName:
                res.append(name)
            for n in self.family[name]:
                dfs(n)
        dfs(self.king)
        return res
