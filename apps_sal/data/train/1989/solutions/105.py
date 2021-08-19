class Solution:
    def longestAwesome(self, s: str) -> int:
        # 相似题目1371
        '''
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
        '''
        # 这道题我想过二分法，但是二分的逻辑是不对的虽然验证很简单。
        # 这道题我想过divide and conquer但是以中间值往两边扩张的最长无法求
        # 最后联想到之前的连续最长问题以及奇偶计数问题可以获得解法O(N)
        res, cur, n = 0, 0, len(s)
        seen = [-1] + [n] * 1024  # 一共10位数码*(选or不选)所以状态数也就1024 + 1个
        for i, c in enumerate(s):
            cur ^= (1 << int(c))
            for a in range(10):
                res = max(res, i - seen[cur ^ (1 << a)])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res
