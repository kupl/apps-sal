class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N <= 1:
            return True

        def paint(node, color):
            if colors[node] is not None:
                return colors[node] != color
            colors[node] = color
            new_color = not color
            for adj_node in g[node]:
                if paint(adj_node, new_color):
                    return True
            return False
        g = collections.defaultdict(list)
        for (a, b) in dislikes:
            g[a].append(b)
            g[b].append(a)
        colors = dict.fromkeys(g, None)
        for n in g:
            if colors[n] is None:
                if paint(n, False):
                    return False
        return True
