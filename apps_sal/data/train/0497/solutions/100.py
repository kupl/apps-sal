
from functools import lru_cache


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        list_jobs = sorted(zip(startTime, endTime, profit))

        @lru_cache(maxsize=None)
        def find(i=0):
            if i >= len(list_jobs):
                return 0
            l = i + 1
            r = len(list_jobs) - 1

            j = len(list_jobs)

            while l <= r:
                middle = (l + r) // 2

                if list_jobs[middle][0] < list_jobs[i][1]:
                    l = middle + 1
                else:
                    r = middle - 1
                    j = middle

            return max(list_jobs[i][2] + find(j), find(i + 1))

        return find()
