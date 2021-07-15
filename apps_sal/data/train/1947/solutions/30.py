class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # Combine counts in B to save time
        count = collections.Counter()
        for b in B:
            # | keeps bigger number
            count |= collections.Counter(b)
        return [a for a in A if (Counter(a) & count) == count]
