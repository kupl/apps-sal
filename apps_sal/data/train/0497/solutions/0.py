class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        dp = [(0, 0)]

        task = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        task = sorted(task, key=lambda x: x[1])

        for s, e, p in task:
            noTaskProf = dp[-1][1]
            for end, pro in reversed(dp):
                if end <= s:
                    doTaskProf = pro + p
                    break
            if doTaskProf > noTaskProf:
                dp.append((e, doTaskProf))
        return dp[-1][1]
