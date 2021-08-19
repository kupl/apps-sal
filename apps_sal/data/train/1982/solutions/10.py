def dfs(adjList, teams, node):
    teams[node] = 1
    stack = [node]
    while stack:
        node = stack.pop()
        team = teams[node]
        for adjNode in adjList[node]:
            if adjNode in teams and teams[adjNode] == team:
                return False
            if adjNode not in teams:
                teams[adjNode] = 1 - team
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
        teams = {}
        for i in range(1, N + 1):
            if i not in teams:
                if not dfs(adjList, teams, i):
                    return False
        return True
