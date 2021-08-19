from collections import Counter


class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A) // 2
        d = Counter(A)
        for (idx, val) in d.items():
            if val == n:
                return idx
        return -1
