class Solution:

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        K = len(n)
        candidates = [str(10 ** k + d) for k in (K - 1, K) for d in (-1, 1)]
        prefix = n[:(K + 1) // 2]
        P = int(prefix)
        for start in map(str, (P - 1, P, P + 1)):
            candidates.append(start + (start[:-1] if K % 2 else start)[::-1])

        def delta(x):
            return abs(int(n) - int(x))
        ans = None
        for cand in candidates:
            if cand != n and (not cand.startswith('00')):
                if ans is None or delta(cand) < delta(ans) or (delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans
