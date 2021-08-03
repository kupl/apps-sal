import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(p):
            return p[0]**2 + p[1]**2

        def qs(l, r, k):
            if l >= r:
                return
            pivotd = dist(points[r])
            ll = l
            for rr in range(l, r):
                if dist(points[rr]) < pivotd:
                    points[ll], points[rr] = points[rr], points[ll]
                    ll += 1
            ppos = ll
            points[ppos], points[r] = points[r], points[ppos]
            if ppos == k:
                return
            if ppos < k:
                qs(ppos + 1, r, k)
            qs(l, ppos - 1, k)

        qs(0, len(points) - 1, K - 1)
        return points[:K]
