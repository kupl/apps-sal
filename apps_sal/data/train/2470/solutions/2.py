class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        lst = [tuple(sorted(d)) for d in dominoes]
        counts = [lst.count(x) for x in set(lst)]
        return int(sum([x * (x - 1) / 2 for x in counts]))
        x = [1, 2, 3]
        y = map(lambda a: a + 2, x)
        print(list(y))
