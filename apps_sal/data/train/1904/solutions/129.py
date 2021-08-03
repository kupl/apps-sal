from collections import defaultdict
import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        lookup = defaultdict(list)

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            lookup[distance].append([x, y])
            heapq.heappush(heap, -distance)
            if len(heap) > K:
                heapq.heappop(heap)
        result = []
        for distance in heap:
            result.append(lookup[-distance].pop())
        return result
