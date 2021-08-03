#
 # [539] Minimum Time Difference
 #
 # https://leetcode.com/problems/minimum-time-difference/description/
 #
 # algorithms
 # Medium (46.11%)
 # Total Accepted:    15.7K
 # Total Submissions: 34.1K
 # Testcase Example:  '["23:59","00:00"]'
 #
 # Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
 # minimum minutes difference between any two time points in the list.
 #
 # Example 1:
 #
 # Input: ["23:59","00:00"]
 # Output: 1
 #
 #
 #
 # Note:
 #
 # The number of time points in the given list is at least 2 and won't exceed
 # 20000.
 # The input time is legal and ranges from 00:00 to 23:59.
 #
 #
 #
 class Solution:
     def findMinDifference(self, timePoints):
         """
         :type timePoints: List[str]
         :rtype: int
         """
         exist = [False] * 1440
         low, high = 1440, 0
         for p in timePoints :
             t = int(p[: 2]) * 60 + int(p[3 :])
             if exist[t] :
                 return 0
             exist[t] = True
             low, high = min(low, t), max(high, t)
         diff = low + 1440 - high
         left, right = low, low + 1
         while left < high :
             while right <= high and not exist[right] :
                 right += 1
             diff = min(diff, right - left)
             left, right = right, right + 1
         return diff

