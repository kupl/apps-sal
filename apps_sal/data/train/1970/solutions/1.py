class Solution:

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        K = len(n)
        candidates = [str(10 ** k + d) for k in (K - 1, K) for d in (-1, 1)]
        Prefix = int(n[:(K + 1) // 2])
        for start in map(str, [Prefix - 1, Prefix, Prefix + 1]):
            candidates.append(str(start) + (start[:-1] if K % 2 == 1 else start)[::-1])
        (ans, diff) = (0, float('inf'))
        base = int(n)
        for C in candidates:
            b = int(C)
            d = abs(b - base)
            if d == 0 or d > diff or (d == diff and b > ans):
                continue
            ans = int(C)
            diff = d
        return str(ans)
