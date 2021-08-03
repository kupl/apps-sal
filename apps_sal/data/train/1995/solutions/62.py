class Solution:
    #     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #         curr_end, max_end = 0, 0
    #         list_curr = []
    #         for trip in trips:
    #             max_end = trip[2]
    #             list_curr.extend([0] * (max_end - curr_end))
    #             # print(len(list_curr))
    #             for _ in range(trip[1], trip[2]):
    #                 list_curr[_] += trip[0]
    #             curr_end = max_end

    #             if max(list_curr) > capacity:
    #                 return False
    #         return True
    # def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #     list_end = []
    #     for _ in trips:
    #         list_end.extend([_[2]])
    #     len_list = max(list_end)
    #     list_curr = [0]*len_list
    #     for trip in trips:
    #         for _ in range(trip[1], trip[2]):
    #             list_curr[_] += trip[0]
    #         if max(list_curr) > capacity:
    #             return False
    #     return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        list_curr = [0] * 1000
        for trip in trips:
            for _ in range(trip[1], trip[2]):
                list_curr[_] += trip[0]
            if max(list_curr) > capacity:
                return False
        return True
