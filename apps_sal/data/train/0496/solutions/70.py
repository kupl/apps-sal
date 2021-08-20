class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:

        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        root = {}
        return sum((find(i) - i for i in A))
