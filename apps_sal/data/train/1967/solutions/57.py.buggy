class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        L, T, t = len(S), \"\", []
        for i in range(1, L - 2):
            for j in range(1, L - i -1):
                if i > 1 and S[0] == '0' or j > 1 and S[i] == '0':
                    continue
                a, b = int(S[:i]), int(S[i:i+j])
                T, t = S[:i+j], [a, b]
                while len(T) < L:
                    c = a + b
                    T += str(c)
                    t += [c]
                    a, b = b, c
                if len(T) == L and T == S and len(t) > 2 and t[-1] < 2**31 -1:
                    return t

        return []
        
