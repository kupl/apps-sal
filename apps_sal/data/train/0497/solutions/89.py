class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        T = []
        for i, s in enumerate(startTime):
            T.append((s, False, i))
        for i, e in enumerate(endTime):
            T.append((e, True, i))
        T = sorted(T)

        best = dict()
        prev = 0
        for t in T:
            time, end, i = t
            if end:
                curr = max(best[startTime[i]] + profit[i], prev)
            else:
                curr = prev
            best[time] = curr
            prev = curr
        return best[T[-1][0]]
