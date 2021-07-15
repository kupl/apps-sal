#
# @lc app=leetcode id=1386 lang=python3
#
# [1386] Cinema Seat Allocation
#
# https://leetcode.com/problems/cinema-seat-allocation/description/
#
# algorithms
# Medium (33.70%)
# Total Accepted:    9K
# Total Submissions: 25.8K
# Testcase Example:  '3\
[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]'
#
#
#
# A cinema  has n  rows of seats, numbered from 1 to n  and there are ten  seats in
# each row, labelled from 1  to 10  as shown in the figure above.
#
# Given the array reservedSeats containing the numbers of seats already
# reserved, for example, reservedSeats[i] = [3,8]  means the seat located in row
# 3 and labelled with 8  is already reserved.
#
# Return the maximum number of four-person groups  you can assign on the cinema
# seats. A four-person group  occupies four  adjacent seats in one single row.
# Seats across an aisle (such as [3,3]  and [3,4]) are not considered to be
# adjacent, but there is an exceptional case  on which an aisle split  a
# four-person group, in that case, the aisle split  a four-person group in the
# middle,  which means to have two people on each side.
#
#
# Example 1:
#
#
#
#
# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows the optimal allocation for four groups,
# where seats mark with blue are already reserved and contiguous seats mark
# with orange are for one group.
#
#
# Example 2:
#
#
# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2
#
#
# Example 3:
#
#
# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
# 1 <=  reservedSeats.length <= min(10*n, 10^4)
# reservedSeats[i].length == 2
# 1  <=  reservedSeats[i][0] <= n
# 1 <=  reservedSeats[i][1] <= 10
# All reservedSeats[i] are distinct.
#
#
#
from typing import List


def calculate_groups(reserved_array):
    \"\"\"
    >>> calculate_groups([0,0,1,1,0,0,0,0,0,1,0,0])
    1

    >>> calculate_groups([0,0,0,0,0,0,1,0,0,0,0,0])
    1

    >>> calculate_groups([0,1,0,0,0,0,0,0,0,0,0,1])
    2

    \"\"\"
    center_seats = 0
    side_seats = 0
    if sum(reserved_array[4:8]) == 0:
        center_seats += 1
    if sum(reserved_array[2:6]) == 0:
        side_seats += 1
    if sum(reserved_array[6:10]) == 0:
        side_seats += 1
    return max(center_seats, side_seats)

class Solution:
    \"\"\"
    >>> Solution().maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])
    4

    >>> Solution().maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]])
    2

    >>> Solution().maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]])
    4

    \"\"\"

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reservedSeats = sorted(reservedSeats, key=lambda i: i[0])
        counter = 0
        row = 1
        reserved = [0] * 11
        while reservedSeats:
            item = reservedSeats.pop(0)
            if item[0] != row:
                missed_rows = item[0] - row - 1
                counter += 2 * missed_rows
                counter += calculate_groups(reserved)
                row = item[0]
                reserved = [0] * 11
                reserved[item[1]] = 1
            else:
                reserved[item[1]] = 1
        counter += calculate_groups(reserved)
        counter += (n - row) * 2
        return counter

