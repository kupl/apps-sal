class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N + 1):
            if N % X == 0:
                if all((v % X == 0 for v in list(count.values()))):
                    return True
        return False
