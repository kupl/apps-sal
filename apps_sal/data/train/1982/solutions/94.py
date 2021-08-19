class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # TODO
        # every connected component must be bipartite
        if len(dislikes) == 0:
            return True
        graph = {}
        for d in dislikes:
            graph[d[0]] = graph.get(d[0], [])
            graph[d[1]] = graph.get(d[1], [])
            graph[d[0]].append(d[1])
            graph[d[1]].append(d[0])
        colors = {}

        visited_set = set()
        for i in range(1, N + 1):
            if i in visited_set:
                continue
            colors[i] = 0
            nodes = [i]
            visited_set.add(i)
            while True:
                # at node i
                new_nodes = []
                for node in nodes:
                    neighbors = graph.get(node)
                    if neighbors is None:
                        continue
                    c = colors[node]
                    nc = c ^ 1
                    for j in neighbors:
                        if j not in colors:
                            colors[j] = nc
                            new_nodes.append(j)
                            visited_set.add(j)
                            continue
                        if colors[j] != nc:
                            return False
                nodes = new_nodes
                if len(nodes) == 0:
                    break

        return True
