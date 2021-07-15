import collections
class Solution:
    @staticmethod
    def binary_search(arr, i):
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= i:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
        
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        mapping = collections.defaultdict(list)
        for i in range(len(startTime)):
            mapping[endTime[i]].append([startTime[i], profit[i]])

        tasks = sorted(list(mapping.items()), key=lambda x : x[0])
        
        dp = [[0, 0]]
        for group in tasks:
            for task in group[1]:
                idx = self.binary_search(dp, task[0]) - 1
                if idx >= 0 and task[1] + dp[idx][1] > dp[-1][1]:
                    if dp[-1][0] == group[0]:
                        dp[-1][1] = task[1] + dp[idx][1]
                    else:
                        dp.append([group[0], task[1] + dp[idx][1]])
        return dp[-1][1]

