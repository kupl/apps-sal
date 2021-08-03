class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def closest(x): return points[x][0]**2 + points[x][1]**2

        def partition(i, j):
            oi = i
            pivot = closest(i)
            i += 1

            while True:
                while i < j and closest(i) < pivot:
                    i += 1
                while i <= j and closest(j) >= pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]
            points[oi], points[j] = points[j], points[oi]
            return j

        def kclosest(i, j, k):
            if i >= j:
                return

            mid = partition(i, j)
            if k > mid - i + 1:
                return kclosest(mid + 1, j, k - (mid - i + 1))
            elif k < mid - i + 1:
                return kclosest(i, mid - 1, k)
        kclosest(0, len(points) - 1, K)
        return points[:K]
