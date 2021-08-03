from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        total_count_B = Counter()
        for s in B:
            total_count_B |= Counter(s)

        return [a for a in A if Counter(a) & total_count_B == total_count_B]
