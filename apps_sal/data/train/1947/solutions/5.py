class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        subset = reduce(operator.or_, (Counter(w) for w in B))
        return [a for a in A if all(a.count(c) >= subset[c] for c in subset.keys())]
