import collections


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_cnt = collections.Counter()
        for b in B:
            b_cnt |= collections.Counter(b)
        res = []
        for a in A:
            if collections.Counter(a) & b_cnt == b_cnt:
                res.append(a)
        return res
