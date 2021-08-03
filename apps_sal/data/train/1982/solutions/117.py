class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def bfsColoring(g, src, colors):
            queue = [src]
            colors[src] = 0

            while queue:
                u = queue.pop(0)
                for v in g[u]:
                    if colors[v] != -1 and colors[v] != 1 - colors[u]:
                        return False
                    elif colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
            print(colors)
            return True

        g = collections.defaultdict(set)

        for dis in dislikes:
            g[dis[0]].add(dis[1])
            g[dis[1]].add(dis[0])

        colors = [-1 for _ in range(N + 1)]
        for i in range(1, N + 1):
            if colors[i] == -1:
                if not bfsColoring(g, i, colors):
                    return False
        print(colors)
        if -1 in set(colors[1:]):
            return False
        return True
