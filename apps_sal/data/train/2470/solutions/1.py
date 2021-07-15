class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        lst = [tuple(sorted(d)) for d in dominoes]
        dct = dict((x,lst.count(x)) for x in set(lst))

        y = sum(list([(x*(x-1)/2) for x in list(dct.values())]))
        return int(y)

