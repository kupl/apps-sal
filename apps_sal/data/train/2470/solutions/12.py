class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_dict = {}
        for i in dominoes:
            j = frozenset(i)
            if j not in dominoes_dict:
                dominoes_dict[j] = 1
            else:
                dominoes_dict[j] += 1

        return sum([int((n * (n - 1)) / 2) for n in list(dominoes_dict.values()) if n > 1])
