class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for point in points:
            d = 0
            for cor in point:
                d += cor**2
            h.append((d, point))

        ksmallests = heapq.nsmallest(K, h)
        ret = []
        for val, point in ksmallests:
            ret.append(point)
        return ret
