class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        c = Counter(A)
        c = list(c.most_common(1))
        return c[0][0]
