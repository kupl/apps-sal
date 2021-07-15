class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        L, T, t = len(S), \"\", []
        for i in range(1,L-2):
        \tfor j in range(1,L-i-1):
        \t\tif (i > 1 and S[0] == '0') or (j > 1 and S[i] == '0'): continue
        \t\ta, b = int(S[:i]), int(S[i:i+j])
        \t\tT, t = S[:i+j], [a,b]
        \t\twhile len(T) < L:
        \t\t\tc = a + b
        \t\t\tT += str(c)
        \t\t\tt += [c]
        \t\t\ta, b = b, c
        \t\tif len(T) == L and T == S and len(t) > 2 and t[-1] < 2**31 - 1: return t
        return []
