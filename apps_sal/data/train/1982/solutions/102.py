class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        for (i, j) in dislikes:
            g[i - 1].append(j - 1)
            g[j - 1].append(i - 1)
        color = [-1] * N
        for i in range(N):
            if color[i] == -1:
                color[i] = 0
                queue = [i]
            while queue:
                u = queue.pop(0)
                for j in g[u]:
                    if color[j] == color[u]:
                        return False
                    if color[j] == -1:
                        queue.append(j)
                        color[j] = 1 - color[u]
        return True
