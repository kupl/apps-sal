class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)
        for (a, b) in red_edges:
            graph_red[a].append(b)
        for (a, b) in blue_edges:
            graph_blue[a].append(b)

        def bfs(target):
            BLUE = 1
            RED = 2
            seen = set()
            queue = deque([(0, 0, BLUE), (0, 0, RED)])
            while queue:
                (node, steps, color) = queue.popleft()
                if node == target:
                    return steps
                if color == RED:
                    for next_node in graph_blue[node]:
                        if (next_node, BLUE) not in seen:
                            seen.add((next_node, BLUE))
                            queue.append((next_node, steps + 1, BLUE))
                else:
                    for next_node in graph_red[node]:
                        if (next_node, RED) not in seen:
                            seen.add((next_node, RED))
                            queue.append((next_node, steps + 1, RED))
            return -1
        res = []
        for i in range(n):
            res.append(bfs(i))
        return res
