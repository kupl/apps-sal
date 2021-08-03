class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        color = dict()

        for i in range(1, N + 1):
            if i not in color:
                if not self.dfs(i, color, graph, c=0):
                    return False
        # print(color)
        return True

    def dfs(self, idx, color, graph, c):
        # print((idx,c))
        color[idx] = c
        newc = 0 if c == 1 else 1
        for i in graph[idx]:
            if i not in color:
                if not self.dfs(i, color, graph, newc):
                    return False
            else:
                if color[i] == color[idx]:
                    return False
        return True
