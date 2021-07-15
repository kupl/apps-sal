class Solution(object):
    def longestAwesome(self, s):
        d = {0: -1}
        cands = {1<<x for x in range(10)}
        cands.add(0)
        cur = 0
        res = 0
        for i, c in enumerate(s):
            cur ^= (1 << int(c))
            for cand in cands:
                res = max(res, i - d.get(cur ^ cand, i))
            if cur not in d:
                d[cur] = i
        return res

