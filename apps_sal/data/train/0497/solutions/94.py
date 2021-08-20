class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        points = list(set(startTime + endTime))
        points.sort()
        dic = defaultdict(list)
        for (start, end, profit) in zip(startTime, endTime, profit):
            dic[end].append([start, profit])
        DP = {points[0]: 0}
        res = 0
        for i in range(1, len(points)):
            DP[points[i]] = DP[points[i - 1]]
            for (start, profit) in dic[points[i]]:
                DP[points[i]] = max(DP[points[i]], DP[start] + profit)
            res = max(res, DP[points[i]])
        return res
