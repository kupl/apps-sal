class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        cc = Counter(A)
        for key in list(cc.keys()):
            if cc[key] == len(A) // 2:
                return key
