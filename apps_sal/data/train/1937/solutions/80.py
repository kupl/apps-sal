class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.dict = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.dict[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        return self.dfs(self.root, [])

    def dfs(self, root, arr):
        if root not in self.dead:
            arr.append(root)
        if root in self.dict:
            for kid in self.dict[root]:
                self.dfs(kid, arr)
        return arr
