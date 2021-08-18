class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.tree = {kingName: [True, []]}

    def birth(self, parentName: str, childName: str) -> None:
        child = [True, []]
        self.tree[childName] = child
        self.tree[parentName][1].append(childName)

    def death(self, name: str) -> None:
        self.tree[name][0] = False

    def getInheritanceOrder(self) -> List[str]:
        result = []

        def dfs(root_name):
            result.append(root_name)
            if self.tree[root_name][1]:
                for child in self.tree[root_name][1]:
                    dfs(child)
        dfs(self.king)
        return [x for x in result if self.tree[x][0]]
