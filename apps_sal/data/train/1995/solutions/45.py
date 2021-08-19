class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #         # time O(max(N, 1001)); space O(1001)
        #         timestamp = [0] * 1001
        #         for trip in trips:
        #             timestamp[trip[1]] += trip[0]
        #             timestamp[trip[2]] -= trip[0]

        #         used = 0
        #         for change in timestamp:
        #             used += change
        #             if used > capacity:
        #                 return False

        #         return True

        # time O(nlogn); space O(n)
        pooling = []
        for num, start, end in trips:
            pooling.extend([[start, num], [end, -num]])
        pooling.sort()

        for loc, num in pooling:
            capacity -= num
            if capacity < 0:
                return False
        return True
