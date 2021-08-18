from math import comb


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashtable = {}
        for d in dominoes:
            new = tuple(sorted(d))
            if(new not in list(hashtable.keys())):
                hashtable[new] = 1
            else:
                hashtable[new] += 1
        counter = 0
        print(hashtable)
        for k, v in list(hashtable.items()):
            if v >= 2:
                counter += (comb(v, 2))

        return counter
