import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        hp = []
        heapq.heapify(hp)
        for x, y in points:
            ds = x**2 + y**2  # distance square
            if len(hp) < K:
                heapq.heappush(hp, (-ds, [x, y]))
            else:
                heapq.heappushpop(hp, (-ds, [x, y]))
        return [xy for ds, xy in hp]
