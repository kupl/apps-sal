#
# @lc app=leetcode id=1362 lang=python3
#
# [1362] Closest Divisors
#
# https://leetcode.com/problems/closest-divisors/description/
#
# algorithms
# Medium (55.74%)
# Total Accepted:    10.2K
# Total Submissions: 17.9K
# Testcase Example:  '8'
#
# Given an integer num, find the closest two integers in absolute difference
# whose product equals num + 1 or num + 2.
#
# Return the two integers in any order.
#
#
# Example 1:
#
#
# Input: num = 8
# Output: [3,3]
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 =
# 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
#
#
# Example 2:
#
#
# Input: num = 123
# Output: [5,25]
#
#
# Example 3:
#
#
# Input: num = 999
# Output: [40,25]
#
#
#
# Constraints:
#
#
# 1 <= num <= 10^9
#
#
#
from math import sqrt
from typing import List
from bisect import bisect_left

def insert(collector, solution):
    insertion_point = bisect_left(collector, abs(solution[0] - solution[1]))
    collector.insert(insertion_point, solution)

class Solution:
    \"\"\"
    >>> Solution().closestDivisors(0)
    [1, 1]

    >>> Solution().closestDivisors(1)
    [1, 2]

    >>> Solution().closestDivisors(8)
    [3, 3]

    >>> Solution().closestDivisors(123)
    [5, 25]

    >>> Solution().closestDivisors(999)
    [25, 40]

    \"\"\"
    def closestDivisors(self, num: int) -> List[int]:
        found_solutions = []
        ref_table = {}
        for i in range(1, int((sqrt(num + 2))) + 1):
            if (num + 1) % i == 0:
                distance = abs(i - (num + 1) // i)
                insertion_point = bisect_left(found_solutions, distance)
                found_solutions.insert(insertion_point, distance)
                ref_table[distance] = (i, (num + 1) // i)
            if (num + 2) % i == 0:
                distance = abs(i - (num + 2) // i)
                insertion_point = bisect_left(found_solutions, distance)
                found_solutions.insert(insertion_point, distance)
                ref_table[distance] = (i, (num + 2) // i)
        return list(ref_table[found_solutions[0]])




