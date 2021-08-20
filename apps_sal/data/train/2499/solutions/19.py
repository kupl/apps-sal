class Solution:

    def fun(m, k, c):
        for i in k:
            if len(i) == m:
                g = len(i) // m
                c += g
            elif len(i) % m == 0:
                c += len(i) // m
        return c

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck.sort()
        l = []
        k = []
        l.append(deck[0])
        for i in range(1, len(deck)):
            if l[-1] != deck[i]:
                k.append(l)
                l = []
            l.append(deck[i])
        k.append(l)
        k.sort()
        j = len(k[0])
        if len(k[-1]) == 1:
            return bool(0)
        for i in range(2, len(deck) + 1):
            c = 0
            c += Solution.fun(i, k, c)
            if len(deck) / i == c:
                return bool(1)
        return bool(0)
