class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        [1,2,0,0,2,1]
        day0 rains on lake1
        day1 rains on lake2
        day2 sunny
        day3 sunny
        day4 rains on lake1
        day5 rains on lake2

        """
        sunny_day_idx = []
        res = [-1] * len(rains)
        for (day, lake) in enumerate(rains):
            if lake == 0:
                sunny_day_idx.append(day)
                res[day] = 1
        last_day_rains_over_lake = {}
        '\n        [1,0,2,0,2,1]\n        for lake2 we need to find sunny_day_idx between 2 - 4\n        sunny_day_idx=[1,4] is a increasing array\n        use binary search to find minimum value between prev_day and curr_day\n        \n        '

        def binary_search(sunny_day_idx, prev):
            (low, high) = (0, len(sunny_day_idx))
            while low < high:
                mid = (low + high) // 2
                if sunny_day_idx[mid] > prev:
                    high = mid
                else:
                    low = mid + 1
            return low if low < len(sunny_day_idx) and sunny_day_idx[low] > prev else None
        print(binary_search([2, 3], 0))
        for (day, lake) in enumerate(rains):
            if lake != 0 and lake not in last_day_rains_over_lake:
                last_day_rains_over_lake[lake] = day
            elif lake != 0 and lake in last_day_rains_over_lake:
                if not sunny_day_idx:
                    return []
                idx = binary_search(sunny_day_idx, last_day_rains_over_lake[lake])
                if idx == None:
                    return []
                if sunny_day_idx[idx] > day:
                    return []
                res[sunny_day_idx[idx]] = lake
                last_day_rains_over_lake[lake] = day
                sunny_day_idx.pop(idx)
        return res
