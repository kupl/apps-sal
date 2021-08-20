class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:

        def bfs(target, color):
            q = deque([[0, 0, color]])
            seen = set()
            while q:
                (cur, step, c) = q.popleft()
                if cur == target:
                    return step
                if (cur, c) in seen:
                    continue
                seen.add((cur, c))
                for neighbor in e[cur][c]:
                    q.append([neighbor, step + 1, (c + 1) % 2])
            return -1
        e = {i: [set(), set()] for i in range(n)}
        for (i, j) in red_edges:
            e[i][0].add(j)
        for (i, j) in blue_edges:
            e[i][1].add(j)
        res = [0] * n
        for i in range(1, n):
            red = bfs(i, 0)
            blue = bfs(i, 1)
            if red == -1:
                res[i] = blue
            elif blue == -1:
                res[i] = red
            else:
                res[i] = min(red, blue)
        return res
