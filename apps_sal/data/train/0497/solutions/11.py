import collections
import functools
import heapq
import itertools
import sys
from functools import lru_cache
from typing import List

'''
n份工作薪水不同，开始时间和结束时间不同，找到最大的收益，时间不能冲突。

背包问题，工作可以做或者不做，做时选择下一个不冲突的工作继续。
'''


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def dfs_func():
            n = len(profit)
            dp = {}
            jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
            jobs.sort()

            def find_next_confict(jobs_i):
                for jobs_j in range(jobs_i + 1, n):
                    if jobs[jobs_i][1] <= jobs[jobs_j][0]:
                        return jobs_j
                return n

            def find_next_confict_left(jobs_i):
                dst = jobs[jobs_i][1]
                left = jobs_i
                right = n
                while left < right:
                    mid = int((left + right) / 2)
                    mid_value = jobs[mid][0]
                    if dst < mid_value:
                        right = mid
                    elif dst > mid_value:
                        left = mid + 1
                    else:
                        right = mid
                return left

            def dfs(jobs_i):
                if jobs_i >= n:
                    return 0
                if jobs_i in dp:
                    return dp[jobs_i]
                s, e, p = jobs[jobs_i]
                jobs_j = find_next_confict_left(jobs_i)
                choose = p
                if jobs_j < n:
                    choose += dfs(jobs_j)
                not_choose = dfs(jobs_i + 1)
                dp[jobs_i] = max(choose, not_choose)
                return dp[jobs_i]

            return dfs(0)

        def dp_func():

            n = len(profit)
            jobs = [(endTime[i], startTime[i], profit[i]) for i in range(n)]
            jobs.sort()
            dp = [0 for _ in range(n + 1)]

            def find_pre_not_confict(jobs_i):
                dst = jobs[jobs_i][1]
                left = 0
                right = jobs_i
                while left < right:
                    mid = int((left + right) / 2)
                    mid_value = jobs[mid][0]
                    if dst < mid_value:
                        right = mid
                    elif dst > mid_value:
                        left = mid + 1
                    else:
                        left = mid + 1
                return left - 1

            def find_pre_not_confict1(jobs_i):
                for i in range(jobs_i, -1, -1):
                    if jobs[jobs_i][1] >= jobs[i][0]:
                        return i
                return -1

            for i in range(1, n + 1):
                last_not_conflict = find_pre_not_confict(i - 1)
                choose = jobs[i - 1][2]
                if last_not_conflict != -1:
                    choose += dp[last_not_conflict + 1]
                dp[i] = max(dp[i - 1], choose)
            return dp[n]
        return dp_func()
