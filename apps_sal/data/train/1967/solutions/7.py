class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        n = len(S)

        for i in range(1, min(32, (n - 1) // 2 + 1)):
            for j in range(i + 1, 2 * n // 3 + 1):
                a, b = int(S[:i]), int(S[i:j])
                idx = len(str(a + b))
                tmp = [a, b]
                l = j
                while int(S[l:l + idx]) == a + b:
                    if int(S[l:l + idx]) > 2 ** 31 - 1:
                        break
                    tmp.append(int(S[l:l + idx]))
                    if l + idx == n:
                        return tmp
                    a = b
                    b = int(S[l:l + idx])
                    l += idx
                    idx = len(str(a + b))
        return []
