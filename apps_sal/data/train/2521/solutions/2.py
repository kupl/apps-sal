class Solution:

    def reformat(self, s: str) -> str:
        cA = []
        cD = []
        for i in s:
            if i.isalpha():
                cA.append(i)
            else:
                cD.append(i)
        res = ''
        if len(s) % 2 == 0:
            if len(cA) == len(cD):
                for i in range(len(cA)):
                    res += cA[i] + cD[i]
        elif abs(len(cA) - len(cD)) == 1:
            if len(cA) > len(cD):
                res = cA[0]
                for i in range(len(cD)):
                    res += cD[i] + cA[i + 1]
            else:
                res = cD[0]
                for i in range(len(cA)):
                    res += cA[i] + cD[i + 1]
        return res
