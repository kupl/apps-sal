class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for e in dislikes:
            (u, v) = e
            graph[u].add(v)
            graph[v].add(u)
        print(graph)
        visited = set()
        a = set()
        b = set()
        for n in range(1, N):
            queue = deque([n])
            while queue:
                u = queue.popleft()
                if u in visited:
                    continue
                visited.add(u)
                if len(graph[u] & a) == 0:
                    a.add(u)
                elif len(graph[u] & b) == 0:
                    b.add(u)
                else:
                    return False
                for v in graph[u]:
                    if v in visited:
                        continue
                    queue.append(v)
        print(a, b)
        return True
