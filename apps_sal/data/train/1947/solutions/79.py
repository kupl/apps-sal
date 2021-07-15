from functools import reduce
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        c_b = reduce(operator.or_, (Counter(w) for w in B))
        return [a for a in A if not c_b-Counter(a)]

