class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum((d * (d - 1) // 2 for d in Counter((tuple(sorted(domino)) for domino in dominoes)).values()))
