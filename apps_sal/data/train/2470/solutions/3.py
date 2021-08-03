class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = collections.Counter()
        for i in dominoes:
            c[tuple(sorted(i))] += 1

        return sum(math.comb(i, 2) for i in c.values())
