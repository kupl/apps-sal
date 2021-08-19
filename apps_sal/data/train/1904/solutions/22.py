import random


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def sort(left, right, K):
            if left < right:
                pivot = partition(left, right)
                if pivot == K:
                    return
                elif pivot < K:
                    sort(pivot + 1, right, K)
                else:
                    sort(left, pivot - 1, K)

        def partition(left, right):
            pivot = points[right]
            anchor = left
            for i in range(left, right):
                if points[i][0] ** 2 + points[i][1] ** 2 <= pivot[0] ** 2 + pivot[1] ** 2:
                    (points[anchor], points[i]) = (points[i], points[anchor])
                    anchor += 1
            (points[anchor], points[right]) = (points[right], points[anchor])
            return anchor
        sort(0, len(points) - 1, K)
        return points[:K]
