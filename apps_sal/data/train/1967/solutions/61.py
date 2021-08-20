class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:

        def getfirst():
            pairs = []
            for i in range(1, len(S) - 2):
                for j in range(i + 1, len(S) - 1):
                    pairs.append((i, j))
            return pairs

        def helper(s, e):
            ans = [S[:s], S[s:e]]
            newS = S[e:]
            while newS:
                nex = int(ans[-1]) + int(ans[-2])
                nex = str(nex)
                if int(nex) >= 2 ** 31:
                    return
                if newS[:len(nex)] == nex:
                    newS = newS[len(nex):]
                    ans += (nex,)
                else:
                    return
            return ans
        pairs = getfirst()
        for (s, e) in pairs:
            ans = helper(s, e)
            if ans:
                return ans
        return []
