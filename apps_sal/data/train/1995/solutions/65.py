import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        #         left = capacity
        #         h = []
        #         trips = sorted(trips, key=lambda x: x[1])

        #         for t in trips:
        #             if h:
        #                 while h and t[1] >= h[0][0]:
        #                     mint = h[0]
        #                     left += mint[1][0]
        #                     heapq.heappop(h)

        #             if left < t[0]:
        #                 return False

        #             heapq.heappush(h, (t[2], t))
        #             left -= t[0]

        #         return True

        path = [0] * 1001
        for t in trips:
            for i in range(t[1], t[2]):
                path[i] += t[0]
                if path[i] > capacity:
                    return False

        return True
