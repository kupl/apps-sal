import heapq


class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0] * 1001
        for t in trips:
            for i in range(t[1], t[2]):
                path[i] += t[0]
                if path[i] > capacity:
                    return False
        return True
