class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        s = []
        for i in range(len(dominoes)):

            dominoes[i] = sorted(dominoes[i])
            if dominoes[i] not in s:
                s.append(dominoes[i])
        re = 0

        def fac(n):
            if n == 0:
                return 1
            if n < 3:
                return n
            return n * fac(n - 1)
        for r in s:
            c = dominoes.count(r)
            re += int(fac(c) / (fac(c - 2) * 2))

        print(dominoes, s, re)
        return re
