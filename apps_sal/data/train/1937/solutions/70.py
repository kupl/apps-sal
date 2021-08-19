class ThroneInheritance:

    def __init__(self, kingName: str):
        self.nation = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.nation[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []

        def dfs(name):
            if name not in self.dead:
                result.append(name)
            for child in self.nation[name]:
                dfs(child)
        dfs(self.king)
        return result
