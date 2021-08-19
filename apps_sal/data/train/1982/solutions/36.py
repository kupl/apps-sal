class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        for d in dislikes:
            edges[d[0]].append(d[1])
            edges[d[1]].append(d[0])

        def dfs(i, col):
            if i in color:
                if color[i] != col:
                    return False
                else:
                    return True
            else:
                color[i] = col
            new = 1 if col == 0 else 0
            for e in edges[i]:
                if not dfs(e, new):
                    return False
            return True
        color = {}
        for i in range(N):
            if i not in color and (not dfs(i, 0)):
                return False
        return True
