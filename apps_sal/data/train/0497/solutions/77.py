class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        srt = sorted(jobs, key=lambda x: x[1])
        print(srt)
        maxp = [j[2] for j in srt]
        n = len(profit)
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if srt[j][1] <= srt[i][0]:
                    maxp[i] = max(srt[i][2] + maxp[j], maxp[i - 1])
                    break
            maxp[i] = max(maxp[i - 1], maxp[i])
        print(maxp)
        return maxp[-1]
