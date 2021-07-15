from functools import reduce
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        alphabet = reduce(lambda x, y: Counter(y) | x, B, Counter())
        return [a for a in A if (Counter(a) & alphabet) == alphabet]

