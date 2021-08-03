class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def add_list(pool, start, end, num):
            for idx in range(start, end):
                pool[idx] += num
        pool = [0] * 1000
        for trip in trips:
            num, start, end = trip
            add_list(pool, start, end, num)
        if max(pool) > capacity:
            return False
        return True
