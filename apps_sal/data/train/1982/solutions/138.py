def dfs(adjList, visited, node):
    teams = {node: 1}
    visited.add(node)
    stack = [node]
    while stack:
        node = stack.pop()
        team = teams[node]
        for adjNode in adjList[node]:
            if adjNode in teams and teams[adjNode] == team:
                return False
            if adjNode not in teams:
                teams[adjNode] = 1 - team
                visited.add(adjNode)
                stack.append(adjNode)
    return True


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        adjList = {i: [] for i in range(1, N + 1)}
        for dislike in dislikes:
            x = dislike[0]
            y = dislike[1]
            adjList[x].append(y)
            adjList[y].append(x)

        visited = set()
        for i in range(1, N + 1):
            if i not in visited:
                if not dfs(adjList, visited, i):
                    return False
        return True
