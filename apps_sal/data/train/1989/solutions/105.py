class Solution:

    def longestAwesome(self, s: str) -> int:
        """
        p = [0]   # 收集累计的 奇偶状态包括0在内
        for c in s:
            x = int(c)
            p.append(p[-1])
            p[-1] ^= 1 << x

        legal = {0}
        for x in range(10):
            legal.add(1 << x)

        first = {}
        ans = 0
        for j, q in enumerate(p):
            for leg in legal:
                ideal = leg ^ q
                i = first.get(ideal, None)
                if i is not None:
                    cand = j - i
                    if cand > ans:
                        ans = cand
            first.setdefault(q, j)
        return ans
        """
        (res, cur, n) = (0, 0, len(s))
        seen = [-1] + [n] * 1024
        for (i, c) in enumerate(s):
            cur ^= 1 << int(c)
            for a in range(10):
                res = max(res, i - seen[cur ^ 1 << a])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res
