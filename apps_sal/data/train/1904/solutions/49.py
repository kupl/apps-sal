class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def compare(p1, p2):
            return p1[0] ** 2 + p1[1] ** 2 - (p2[0] ** 2 + p2[1] ** 2)

        def quickSelect(l, r):
            pivot = points[r]
            j = l
            for i in range(l, r):
                if compare(points[i], pivot) <= 0:
                    (points[i], points[j]) = (points[j], points[i])
                    j += 1
            (points[r], points[j]) = (points[j], points[r])
            return j
        (l, r) = (0, len(points) - 1)
        while l <= r:
            pivot = quickSelect(l, r)
            if pivot == K:
                break
            elif pivot < K:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:K]
