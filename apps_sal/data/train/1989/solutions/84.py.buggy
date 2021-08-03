class Solution(object):
    def longestAwesome(self, s):
        \"\"\"
        :type s: str
        :rtype: int
        \"\"\"
        D = {}
        curr = [0 for _ in range(10)]
        res = 0
        for i, c in enumerate(s):
            c = int(c)
            curr[c] = (curr[c] + 1) % 2
            tc = tuple(curr)
            cand = 0
            if sum(curr) <= 1:
                cand = i + 1
            else:                
                if tc in D:
                    cand = i - D[tc]
                for j in range(10):
                    curr[j] = (1 + curr[j]) % 2
                    oc = tuple(curr)
                    if oc in D:
                        cand = max(cand, i - D[oc])
                    curr[j] = (1 + curr[j]) % 2
            res = max(res, cand)
            if tc not in D:
                D[tc] = i
        return res
