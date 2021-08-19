from collections import defaultdict as dict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = dict(list)
        self.visited = {}
        self.death_set = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        if parentName not in list(self.visited.keys()):
            self.visited[parentName] = False
        if childName not in list(self.visited.keys()):
            self.visited[childName] = False

    def death(self, name: str) -> None:
        self.death_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        stack = []
        u = self.kingName
        self.get_dfs(u, self.visited, self.graph, stack)
        self.reset_visit(self.visited)
        return stack

    def get_dfs(self, u, visited, graph, stack):
        visited[u] = True
        if u not in self.death_set:
            stack.append(u)
        for v in graph[u]:
            if visited[v] == False:
                self.get_dfs(v, visited, graph, stack)

    def reset_visit(self, visited):
        for key in list(visited.keys()):
            visited[key] = False
