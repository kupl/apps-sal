class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        set1 = {}
        sum1 = 0
        for i in dominoes:
            ri = list(reversed(i))
            i = tuple(i)
            ri = tuple(ri)
            if i in set1.keys():
                sum1 += set1[i]
                set1[i] += 1
            elif ri in set1.keys():
                sum1 += set1[ri]
                set1[ri] += 1
            else:
                set1[i] = 1
        return sum1
