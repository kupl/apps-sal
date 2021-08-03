# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

from typing import List
from collections import Counter


class Solution:
    def minIncrementForUnique_bruteforce(self, A: List[int]) -> int:
        counts = Counter(A)
        tot_count = 0

        for n in A:
            while counts[n] > 1:
                counts[n] -= 1
                n += 1
                counts[n] += 1
                tot_count += 1

        return tot_count

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        counts = Counter(A)

        count = 0

        taken = []

        for i in range(100000):
            if counts[i] >= 2:
                taken.extend([i for _ in range(counts[i] - 1)])

            elif taken and counts[i] == 0:
                count += i - taken.pop()

        return count
