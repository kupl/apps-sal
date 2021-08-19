from collections import defaultdict
import heapq


class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = defaultdict(dict)
        for (ii, jj, kk) in edges:
            g[ii][jj] = g[jj][ii] = kk
        (queue, flag) = ([(0, 0)], {0: 0})
        used = {}
        res = 0
        while queue:
            (d, head) = heapq.heappop(queue)
            if d > flag.get(head):
                continue
            res += 1
            for (kk, vv) in list(g[head].items()):
                v = min(vv, M - d)
                used[head, kk] = v
                now_d = d + vv + 1
                if now_d < flag.get(kk, M + 1):
                    heapq.heappush(queue, (now_d, kk))
                    flag[kk] = now_d
        for (ii, jj, kk) in edges:
            res += min(kk, used.get((ii, jj), 0) + used.get((jj, ii), 0))
        return res
