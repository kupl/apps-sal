class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        a = rains
        n = len(a)
        j = 0
        ans = [-1] * n
        v = {}
        q = []
        for i in range(n):
            c = a[i]
            if c:
                if c in v:
                    j = bisect.bisect(q, v[c])
                    if j == len(q):
                        return []
                    else:
                        ans[q[j]] = c
                        q.pop(j)
                v[c] = i
            else:
                q.append(i)
        while q:
            ans[q.pop()] = 1
        return ans
