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
            a = 5
            return ht[N]

        fact = findFactors(N)

        ht[N] = False
        for num in fact:
            ht[N] = ht[N] or self.helper(N - num, numRds + 1, ht)

        return ht[N]


def findFactors(num: int) -> list:
    res = []
    for val in range(1, num):
        if num % val == 0:
            res.append(val)
    return res
