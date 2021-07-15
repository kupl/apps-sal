class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        color = [-1 for _ in range(N + 1)]
        g = collections.defaultdict(set)
        for a, b in dislikes:
            g[a].add(b)
            g[b].add(a)
        visited = set()
        for i in range(1, N + 1):
            if i not in visited:
                q = collections.deque()
                q.append(i)
                visited.add(i)
                color[i] = 0
                while q:
                    size = len(q)
                    while size > 0:
                        node = q.popleft()
                        for nei in g[node]:
                            if nei not in visited:
                                q.append(nei)
                                visited.add(nei)
                                color[nei] = 1 - color[node]
                            else:
                                if color[nei] != 1 - color[node]:
                                    return False
                        size -= 1
        return len(set(color)) == 3
