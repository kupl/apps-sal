class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_dict = {}
        for i in [frozenset(domino) for domino in dominoes]:
            if i not in dominoes_dict:
                dominoes_dict[i] = 1
            else:
                dominoes_dict[i] += 1
        return sum([int(n * (n - 1) / 2) for n in list(dominoes_dict.values()) if n > 1])
