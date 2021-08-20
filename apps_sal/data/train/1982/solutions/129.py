class Solution:

    def isbi(self, i, color):
        q = []
        q.append(i)
        color[i] = 1
        while q:
            curr = q.pop(0)
            for j in self.graph[curr]:
                if color[j] == color[curr]:
                    return False
                if color[j] == -1:
                    color[j] = 1 - color[curr]
                    q.append(j)
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        for (v, u) in dislikes:
            self.graph[v].append(u)
            self.graph[u].append(v)
        color = [-1] * (N + 1)
        for i in range(1, N + 1):
            if color[i] == -1:
                if not self.isbi(i, color):
                    return False
        return True
