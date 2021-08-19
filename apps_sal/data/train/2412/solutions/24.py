class Solution:

    def removeDuplicates(self, S: str) -> str:
        if len(S) < 2:
            return S
        newS = ''
        count = 1
        while len(S) > 1:
            newS = ''
            chain = False
            for i in range(1, len(S)):
                if S[i] != S[i - 1]:
                    if not chain:
                        newS += S[i - 1]
                    elif count % 2 == 1:
                        newS += S[i - 1]
                    chain = False
                    count = 1
                else:
                    chain = True
                    count += 1
            if not chain:
                newS += S[-1]
            elif count % 2 == 1:
                newS += S[-1]
            if newS == S:
                return S
            S = newS
        return S
