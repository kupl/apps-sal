from collections import defaultdict


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for (_from, to) in dislikes:
            graph[_from].append(to)
            graph[to].append(_from)
        colors = {}
        for i in range(1, N + 1):
            if i not in colors and i <= len(graph) - 1:
                stack = [(i, True)]
                while stack:
                    (keys, color) = stack.pop()
                    colors[keys] = color
                    for adj in graph[keys]:
                        if adj in colors:
                            if colors[adj] == colors[keys]:
                                return False
                        else:
                            stack.append((adj, not colors[keys]))
        return all([colors[i] != all((colors[j] for j in graph[i])) for i in colors if graph[i] != []])
