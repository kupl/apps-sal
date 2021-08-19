import random


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def dist(x):
            return points[x][0] ** 2 + points[x][1] ** 2

        def partial_sort(i, j, K):
            if i >= j:
                return
            pivot = random.randint(i, j)
            (points[i], points[pivot]) = (points[pivot], points[i])
            num_sorted = partition(i, j)
            if K < num_sorted + 1 - i:
                partial_sort(i, num_sorted - 1, K)
            elif K > num_sorted + 1 - i:
                partial_sort(num_sorted + 1, j, K - (num_sorted + 1 - i))

        def partition(i, j):
            oi = i
            i += 1
            while True:
                while i < j and dist(i) < dist(oi):
                    i += 1
                while j >= i and dist(j) >= dist(oi):
                    j -= 1
                if i >= j:
                    break
                (points[i], points[j]) = (points[j], points[i])
            (points[oi], points[j]) = (points[j], points[oi])
            return j
        partial_sort(0, len(points) - 1, K)
        return points[:K]
