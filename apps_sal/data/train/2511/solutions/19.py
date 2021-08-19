from collections import Counter


class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        ct = Counter(A)
        return ct.most_common(1)[0][0]
