class Solution:
    def hasGroupsSizeX(self, deck):
        count = Counter(deck)
        N = len(deck)
       # for X in range(2, N+1):
       #     if N % X == 0:
       #         if all(v % X == 0 for v in count.values()):
       #             return True
        g = lambda X: all(v % X == 0 for v in count.values())
        f = lambda X: not N % X and g(X)
        return any(map(f, range(2, N+1)))
        return False
