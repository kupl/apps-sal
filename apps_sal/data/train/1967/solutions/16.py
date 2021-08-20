class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:

        def check(i, a, b):
            if int(a) > 2147483647 or int(b) > 2147483647:
                return ([], False)
            if i == len(S):
                return ([str(a), str(b)], True)
            s = str(a + b)
            if S[i:i + len(s)] == s:
                (out, good) = check(i + len(s), b, int(s))
                if good:
                    return ([str(a)] + out, True)
            return ([], False)
        for i in range(len(S) - 2):
            a = int(S[:i + 1])
            if S[0] == '0' and a != 0:
                break
            for j in range(i + 1, len(S) - 1):
                b = int(S[i + 1:j + 1])
                if S[i + 1] == '0' and b != 0:
                    break
                (out, _) = check(j + 1, a, b)
                if out:
                    return out
        return []
