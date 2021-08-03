import random
import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def euclidean(x): return math.sqrt(x[0]**2 + x[1]**2)

        def topK(arr, l, r, k):
            if l >= r:
                return

            choice = random.randint(l, r)
            arr[l], arr[choice] = arr[choice], arr[l]

            tl, tr = l + 1, r
            while tl <= tr:
                if euclidean(arr[tl]) < euclidean(arr[l]):
                    tl += 1
                    continue
                if euclidean(arr[tl]) >= euclidean(arr[l]):
                    arr[tl], arr[tr] = arr[tr], arr[tl]
                    tr -= 1
                    continue
            arr[l], arr[tr] = arr[tr], arr[l]

            partition = tr

            if (partition - l + 1) <= k:
                topK(arr, partition + 1, r, k - (partition - l + 1))
            else:
                topK(arr, l, partition - 1, k)

        topK(points, 0, len(points) - 1, K)
        return points[:K]
