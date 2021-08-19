import collections


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bCount = collections.Counter()
        for b in B:
            bCount = bCount | collections.Counter(b)
        res = []
        for a in A:
            if collections.Counter(a) & bCount == bCount:
                res += (a,)
        return res
