class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        people = list(graph.keys())
        belongs = [None] * (N+1)
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * (N+1)
        queue = collections.deque()

        for u in people:
            if color[u] == WHITE:
                color[u] = GRAY
                queue.append(u)
                belongs[u] = 1

                while queue:
                    v = queue.popleft()

                    for w in graph[v]:
                        if color[w] == WHITE:
                            color[w] = GRAY
                            queue.append(w)
                            belongs[w] = belongs[v] * -1
                        elif belongs[w] == belongs[v]:
                            return False

                    color[v] = BLACK

        return True
