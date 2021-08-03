class Solution:
    import collections

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        count = collections.Counter()
        for b in B:
            count = count | collections.Counter(b)
        return [a for a in A if Counter(a) & count == count]
