class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        def add_list(pool, start, end, num):
            for idx in range(start, end):
                pool[idx] += num
                if pool[idx] > capacity:
                    return False
        pool = [0] * 1000
        for trip in trips:
            (num, start, end) = trip
            is_false = add_list(pool, start, end, num)
            if is_false == False:
                return False
        return True
