class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        last_dict = {}
        for i in range(len(startTime)):
            if endTime[i] not in last_dict:
                last_dict[endTime[i]] = []
            last_dict[endTime[i]].append((startTime[i], profit[i]))
        last_end = max(endTime)
        result = [0]*(last_end+1)
        
        for t in range(1, len(result)):
            max_val = result[t-1]
            if t in last_dict:
                for (start, profit) in last_dict[t]:
                    # print(last_dict[t])
                    max_val = max(result[start] + profit, max_val)
            result[t] = max_val
        return result[-1]

