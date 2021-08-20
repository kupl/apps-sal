class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = collections.defaultdict(list)
        self.deaths = set()
        self.root = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []

        def dfs(node, result):
            if node not in self.deaths:
                result.append(node)
            children = self.graph[node]
            for child in children:
                dfs(child, result)
        dfs(self.root, result)
        return result
