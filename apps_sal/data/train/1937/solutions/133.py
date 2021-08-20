class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.tree = {kingName: [True, []]}

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName][1].append(childName)
        self.tree[childName] = [True, []]

    def death(self, name: str) -> None:
        self.tree[name][0] = False

    def dfs(self, name):
        if self.tree[name][0]:
            yield name
        for child in self.tree[name][1]:
            yield from self.dfs(child)

    def getInheritanceOrder(self) -> List[str]:
        return list(self.dfs(self.king))
