import collections


class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1:
            return False
        dict1 = collections.Counter(deck)
        for i in range(2, len(deck) + 1):
            if all((v % i == 0 for v in list(dict1.values()))):
                return True
        return False
