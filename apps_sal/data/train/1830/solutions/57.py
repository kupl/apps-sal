from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1]*len(rains)
        zeros = SortedList()
        todry = {}
        for i, r in enumerate(rains):
            if r == 0:
                zeros.add(i)
                continue
            if r in todry:
                di = zeros.bisect_left(todry[r])
                if di >= len(zeros):
                    return []
                ans[zeros[di]] = r
                zeros.pop(di)
            todry[r] = i
        for i in range(len(rains)):
            if rains[i] == 0 and ans[i] == -1:
                ans[i] = 1
        return ans

