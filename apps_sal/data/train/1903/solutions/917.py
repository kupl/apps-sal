class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist.append([d, i, j])
        dist.sort()
        graph = {i: set() for i in range(len(points))}

        def has_cycle(node, prev, parent):
            if node in prev:
                return True
            prev.add(node)
            for next_node in graph[node]:
                if next_node != parent and next_node in prev:
                    return True
                if next_node != parent and has_cycle(next_node, prev, node):
                    return True
            return False
        cost = 0
        n_edge = 0
        for (d, i, j) in dist:
            if n_edge == len(points) - 1:
                break
            graph[i].add(j)
            graph[j].add(i)
            if not has_cycle(i, set(), None) and (not has_cycle(j, set(), None)):
                n_edge += 1
                cost += d
            else:
                graph[i].remove(j)
                graph[j].remove(i)
        return cost
