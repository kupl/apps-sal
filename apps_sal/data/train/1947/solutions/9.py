from collections import Counter


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = set()
        B_count = Counter()
        for b in B:
            word_count = Counter(b)
            for (c, v) in word_count.items():
                B_count[c] = max(B_count[c], v)
        for a in A:
            if len(B_count - Counter(a)) == 0:
                res.add(a)
        return list(res)
