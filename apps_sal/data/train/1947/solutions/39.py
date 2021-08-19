from collections import Counter


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        c = Counter()
        for b in B:
            c = c | Counter(b)
        return [a for a in A if Counter(a) & c == c]
