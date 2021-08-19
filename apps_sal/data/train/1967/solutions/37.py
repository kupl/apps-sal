class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        if len(S) < 3:
            return []
        for i in range(1, len(S) - 2):
            first = S[:i]
            for j in range(i, len(S) - 1):
                j += 1
                second = S[i:j]
                split = self.dfs(first, second, S[j:], [first, second])
                if split:
                    return split
        return []

    def notvalid(self, s):
        if int(s) != 0 and s[0] == 0:
            return True
        if int(s) > 2 ** 31 - 1:
            return True
        return False

    def dfs(self, s1, s2, rem, seq):
        if self.notvalid(s1) or self.notvalid(s2):
            return []
        s3 = str(int(s1) + int(s2))
        if self.notvalid(s3):
            return []
        l = len(s3)
        if rem[:l] == s3:
            seq.append(s3)
            if len(rem) > l:
                return self.dfs(s2, s3, rem[l:], seq)
            else:
                return seq
        return []
