class Solution:\r
    def eventualSafeNodes(self, graph):\r
        def dfs(i):\r
            # return false if cyclic\r
            colors[i] = 1  # checking, set color to \"gray\"\r
            # scan all the neighbor\r
            for v in graph[i]:\r
                if colors[v] == 1:\r
                    # cycle detected\r
                    return False\r
                if colors[v] == 0 and dfs(v) == False:\r
                    return False\r
            res.append(i)\r
            colors[i] = 2\r
            return True\r
\r
        colors = [0] * len(graph)\r
        res = []\r
\r
        for i, neighbors in enumerate(graph):\r
            if not colors[i]:\r
                dfs(i)\r
\r
        return sorted(res)\r
\r

