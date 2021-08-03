class Solution:
    def removeDuplicates(self, S: str) -> str:
        count = 1
        S = list(S)
        while count != 0:
            x = 0
            while x < (len(S) - 1):
                if S[x] == S[x + 1]:
                    S.pop(x)
                    S.pop(x)
                    if x > 0:
                        x -= 1
                    count += 1
                x += 1
            if count > 1:
                count = 1
            else:
                count = 0
        return(''.join(S))
