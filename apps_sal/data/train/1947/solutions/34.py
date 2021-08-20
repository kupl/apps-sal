class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        maxcb = Counter()
        for b in B:
            maxcb |= Counter(b)
        return [a for a in A if Counter(a) & maxcb == maxcb]
