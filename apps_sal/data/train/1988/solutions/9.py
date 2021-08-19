class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        radj = [set() for i in range(n)]
        badj = [set() for i in range(n)]
        for (x, y) in red_edges:
            radj[x].add(y)
        for (x, y) in blue_edges:
            badj[x].add(y)

        def bfs(target):
            rv = set()
            bv = set()
            from collections import deque
            que = deque([(0, -1, 0)])
            while len(que) > 0:
                (n, c, r) = que.popleft()
                if c == -1:
                    if target in radj[n] or target in badj[n]:
                        return r + 1
                    for i in radj[n]:
                        que.append((i, 0, r + 1))
                        rv.add(i)
                    for i in badj[n]:
                        que.append((i, 1, r + 1))
                        bv.add(i)
                if c == 0:
                    if target in badj[n]:
                        return r + 1
                    for i in badj[n]:
                        if i not in bv:
                            bv.add(i)
                            que.append((i, 1, r + 1))
                if c == 1:
                    if target in radj[n]:
                        return r + 1
                    for i in radj[n]:
                        if i not in rv:
                            rv.add(i)
                            que.append((i, 0, r + 1))
            return -1
        res = [0] * n
        for x in range(1, n):
            res[x] = bfs(x)
        return res
