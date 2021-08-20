class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        N = len(S)
        for (i, j) in itertools.combinations(range(1, N), 2):
            (a, b) = (S[:i], S[i:j])
            if str(int(a)) != a or str(int(b)) != b or int(a) > 2 ** 31 - 1 or (int(b) > 2 ** 31 - 1):
                continue
            res = []
            res.append(a)
            while j < N:
                c = str(int(a) + int(b))
                if not S.startswith(c, j) or int(c) > 2 ** 31 - 1:
                    res = []
                    break
                res.append(b)
                (a, b) = (b, c)
                j += len(c)
            res.append(c)
            if j == N:
                return res
        return []
