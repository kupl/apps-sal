from collections import Counter


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        counter_b = Counter()
        for b in B:
            tmp = Counter(b)
            for t in tmp:
                counter_b[t] = max(counter_b[t], tmp[t])
        for a in A:
            count = Counter(a)
            invalid = False
            for c in counter_b:
                if count[c] < counter_b[c]:
                    invalid = True
            if not invalid:
                res.append(a)
        return res
