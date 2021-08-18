class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [set() for _ in range(N + 1)]
        for a, b in dislikes:
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)

        colors = [0] * N
        q = []
        for i in range(N):
            if colors[i] != 0:
                continue
            q.append(i)
            colors[i] = 1
            while q:
                cur = q.pop()
                for nxt in graph[cur]:
                    if colors[nxt] == colors[cur]:
                        return False
                    if colors[nxt] == 0:
                        colors[nxt] = -colors[cur]
                        q.append(nxt)
        return True
