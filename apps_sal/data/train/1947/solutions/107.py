class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        subset = {}
        for b in B:
            for char in b:
                subset[char] = max(b.count(char), subset.get(char, 0))

        return [a for a in A if all(a.count(char) >= subset[char] for char in subset.keys())]
