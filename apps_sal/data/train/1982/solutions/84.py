class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        graph = {}
        for d in dislikes:
            graph[d[0]] = graph.get(d[0], [])
            graph[d[1]] = graph.get(d[1], [])
            graph[d[0]].append(d[1])
            graph[d[1]].append(d[0])
        colors = {}

        def dfs(node, c=0):
            if node in colors:
                return colors[node] == c
            colors[node] = c
            nc = c ^ 1
            if graph.get(node):
                return all((dfs(neigh, nc) for neigh in graph[node]))
            return True
        return all((dfs(i, 0) for i in range(1, N + 1) if i not in colors))
        'visited_set = set()\n        for i in range(1, N+1):\n            if i in visited_set:\n                continue\n            colors[i] = 0\n            nodes = [i]\n            visited_set.add(i)\n            while True:\n                # at node i\n                new_nodes = []\n                for node in nodes:\n                    neighbors = graph.get(node)\n                    if neighbors is None:\n                        continue\n                    c = colors[node]\n                    nc = c ^ 1\n                    for j in neighbors:\n                        if j not in colors:\n                            colors[j] = nc\n                            new_nodes.append(j)\n                            visited_set.add(j)\n                            continue\n                        if colors[j] != nc:\n                            return False\n                nodes = new_nodes\n                if len(nodes) == 0:\n                    break\n        \n        return True'
