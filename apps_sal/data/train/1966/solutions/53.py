class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        a = mat
        m, n = len(a), len(a[0])
        def hist(h):
            ret = [0] * n
            s = []
            for i, x in enumerate(h):
                while s and h[s[-1]] >= x:
                    s.pop()
                if s:
                    j = s[-1]
                    ret[i] = ret[j] + (i - j) * x
                else:
                    ret[i] = (i + 1) * x
                s.append(i)
            return sum(ret)
        h = [0] * n
        ans = 0
        for row in a:
            for j in range(n):
                h[j] = row[j] + h[j] if row[j] else 0
            ans += hist(h)
        return ans

