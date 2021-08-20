class Solution:

    def divisorGame(self, N: int) -> bool:
        table = dict()
        res = self.helper(N, 0, table)
        return res

    def helper(self, N: int, numRds: int, ht: dict) -> bool:
        soln = False
        if N == 1 and numRds % 2 == 0:
            return False
        if N == 1 and numRds % 2 != 0:
            return True
        if ht.get(N, None) != None:
            return ht[N]
        ht[N] = False
        fact = findFactors(N)
        for num in fact:
            ht[N] = ht[N] or self.helper(N - num, numRds + 1, ht)
        return ht[N]


def findFactors(num: int) -> list:
    res = []
    (loPtr, hiPtr) = (1, num)
    while hiPtr > loPtr:
        if num % loPtr == 0:
            res.append(loPtr)
            if num // loPtr != num:
                res.append(num // loPtr)
            hiPtr = num // loPtr
        loPtr += 1
    return res
