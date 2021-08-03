class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        time_line, sz, time_mapping, f = [], len(profit), {}, [0] * (2 * len(profit))
        for i in range(sz):
            time_line.append((startTime[i], sz))
            time_line.append((endTime[i], i))
        for index, entry in enumerate(sorted(time_line)):
            if entry[1] < sz:
                f[index] = max(f[index - 1], f[time_mapping[startTime[entry[1]]]] + profit[entry[1]])
            else:
                f[index] = f[index - 1]
                time_mapping[entry[0]] = index
        return f[-1]
