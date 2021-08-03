class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)

        for i, j in itertools.combinations(range(1, n), 2):
            res = []
            a, b = S[:i], S[i:j]
            # if b != str(int(b)):
            if a != str(int(a)) or b != str(int(b)):
                continue
            res.append(int(a))
            res.append(int(b))
            while j < n:
                c = str(int(a) + int(b))
                if not S.startswith(c, j):
                    break
                res.append(int(c))
                j += len(c)
                a, b = b, c
            if j == n:
                for item in res:
                    if item > 2**31 - 1:
                        return []
                return res
        return []
