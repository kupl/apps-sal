class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        subset = {}
        for b in B:
            for char in b:
                subset[char] = max(subset.get(char, 0), b.count(char))
        return [a for a in A if all(a.count(c) >= subset[c] for c in subset.keys())]
