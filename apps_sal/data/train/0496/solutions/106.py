class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        root = {}

        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        return sum((find(a) - a for a in A))
