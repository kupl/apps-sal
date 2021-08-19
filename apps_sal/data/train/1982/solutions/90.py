class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for (start, end) in dislikes:
            edges[start].append(end)
            edges[end].append(start)
        colored = {}
        for i in range(1, 1 + N):
            if i not in colored:
                color = 1
                if not self.get_colors(edges, i, color, colored):
                    return False
        return True

    def get_colors(self, edges, start, color, colored):
        q = [(start, color)]
        while len(q) > 0:
            (node, col) = q.pop(0)
            if node in colored:
                if colored[node] != col:
                    return False
                continue
            colored[node] = col
            new_col = 0 if col == 1 else 1
            for vert in edges[node]:
                q.append((vert, new_col))
        return True
