from functools import reduce


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        c_a = [Counter(w) for w in A]
        c_b = reduce(lambda x, y: x | y, [Counter(w) for w in B])
        return [word for i, word in enumerate(A) if not c_b - c_a[i]]
