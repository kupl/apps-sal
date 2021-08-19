class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        for rain in rains:
            if rain > 0:
                res.append(-1)
            else:
                res.append(1)
        full_lakes = defaultdict(list)
        sunny_days = []
        start = 0
        end = len(rains) - 1
        while rains[start] == 0:
            start += 1
        while rains[end] == 0:
            end -= 1

        def binarySearch(sunny_days, prev_rain, curr):
            if not sunny_days:
                return -1
            low = 0
            high = len(sunny_days)
            while low < high:
                mid = (low + high) // 2
                if sunny_days[mid] <= prev_rain:
                    low = mid + 1
                else:
                    high = mid
            if low >= len(sunny_days) or sunny_days[low] <= prev_rain or sunny_days[low] >= curr:
                return -1
            else:
                return low
        for i in range(start, end + 1):
            if rains[i] != 0:
                if rains[i] not in full_lakes or not full_lakes[rains[i]]:
                    full_lakes[rains[i]].append(i)
                else:
                    prev_rain = full_lakes[rains[i]][-1]
                    if not sunny_days:
                        return []
                    idx = binarySearch(sunny_days, prev_rain, i)
                    if idx == -1:
                        return []
                    else:
                        res[sunny_days[idx]] = rains[i]
                        full_lakes[rains[i]].pop()
                        full_lakes[rains[i]].append(i)
                        sunny_days.pop(idx)
            else:
                sunny_days.append(i)
        return res
