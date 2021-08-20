class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N <= 1:
            return True

        def paint(node, color):
            if colors[node] != -1:
                return colors[node] != color
            colors[node] = color
            for adj_node in g[node]:
                if paint(adj_node, (color + 1) % 2):
                    return True
            return False
        g = collections.defaultdict(list)
        for (a, b) in dislikes:
            g[a].append(b)
            g[b].append(a)
        colors = dict.fromkeys(g, -1)
        for n in g:
            if colors[n] == -1:
                if paint(n, 0):
                    return False
        return True
