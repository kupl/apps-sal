class Solution:
    def hasGroupsSizeX(self, deck):
        count = Counter(deck)
        N = len(deck)
       # for X in range(2, N+1):
       #     if N % X == 0:
       #         if all(v % X == 0 for v in count.values()):
       #             return True
        def g(X): return all(v % X == 0 for v in count.values())
        def f(X): return not N % X and g(X)
        return any(map(f, range(2, N + 1)))
        return False
