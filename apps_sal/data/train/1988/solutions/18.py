class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        #    red -> True
        hRed = defaultdict(list)
        for edge in red_edges:
            hRed[edge[0]].append(edge[1])
        hBlue = defaultdict(list)
        for edge in blue_edges:
            hBlue[edge[0]].append(edge[1])

        def helper(n, curr, visited):
            dist = 0
            small = float('inf')
            if curr:
                arr = deque(hRed[0])
            else:
                arr = deque(hBlue[0])
            while arr:
                size = len(arr)
                for j in range(size):
                    node = arr.popleft()
                    if (node, not curr) not in visited:
                        visited.add((node, not curr))
                        if node == i:
                            small, arr = dist + 1, []
                            break
                        if curr:
                            if node in hBlue:
                                arr += hBlue[node]
                        else:
                            if node in hRed:
                                arr += hRed[node]
                dist += 1
                curr = not curr
            return small
        res = [0]
        for i in range(1, n):
            small = helper(i, True, {(0, True)})
            small = min(small, helper(i, False, {(0, False)}))
            if small == float('inf'):
                res.append(-1)
            else:
                res.append(small)
        return res
