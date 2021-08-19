class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        roots = {}

        def find(k):
            roots[k] = k if k not in roots else find(roots[k] + 1)
            return roots[k]
        return sum((find(a) - a for a in A))
