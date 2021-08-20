class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        for (i, l) in enumerate(S):
            if str(int(S[:i + 1])) == S[:i + 1]:
                for j in range(i + 1, len(S) - 1):
                    if str(int(S[i + 1:j + 1])) == S[i + 1:j + 1]:
                        (pre, cur) = (int(S[:i + 1]), int(S[i + 1:j + 1]))
                        res = [pre, cur]
                        start = j + 1
                        while S.startswith(str(pre + cur), start):
                            length = len(str(pre + cur))
                            (pre, cur) = (cur, int(S[start:start + length]))
                            res += (cur,)
                            start += length
                            if start >= len(S):
                                return res
                            if pre + cur >= 2 ** 31:
                                break
        return []
