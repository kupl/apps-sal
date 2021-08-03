\"\"\"
Leetcode :: 1542. Find Longest Awesome Substring
https://leetcode.com/contest/biweekly-contest-32/problems/find-longest-awesome-substring/
\"\"\"
from math import inf

class Solution:
    def longestAwesome(self, s: str) -> int:
        # A substring of 1 is a palindrome.
        soln = 0
        # Minimum index of this bitmask's occurrence
        bitmask_occurred = [inf for _ in range(pow(2, 10))]
        # Zero occurs before the first letter of s.
        bitmask_occurred[0] = -1 

        # Bit mask prefix
        mask = 0

        # Find the maximum length substring that can be a palindrome.
        for i, c in enumerate(s):
            # Convert c to a number
            n = ord(c) - ord('0')
            # Update bitmask prefix
            mask ^=  (1 << n)

            # Update bitmask's occurrence
            bitmask_occurred[mask] = min(bitmask_occurred[mask], i)

            # If we have seen this bitmask before, then the substring
            # between this occurrence and the minimum previous occurrence
            # is a palindrome.  This will catch *even* length substrings.
            soln = max(soln, i - bitmask_occurred[mask])

            # For odd length substrings, flip each on bit and see if that
            # bitmask occurred before.
            for b in range(10):
                soln = max(soln, i - bitmask_occurred[mask ^ (1 << b)])

        return soln

