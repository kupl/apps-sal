class Solution:
    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        pa = [0] * (n + 1)
        pb = [0] * (n + 1)
        for i in range(n + 1):
            pa[i] = i
            pb[i] = i

        def p(x):
            if x == pa[x]:
                return x
            pa[x] = p(pa[x])
            return pa[x]

        def pp(x):
            if x == pb[x]:
                return x
            pb[x] = pp(pb[x])
            return pb[x]
        ans = 0
        for x in e:
            if x[0] == 3:
                q = p(x[1])
                w = p(x[2])

                r = pp(x[1])
                t = pp(x[2])

                if (q == w and r == t):
                    ans += 1
                else:
                    pa[q] = w
                    pb[r] = t

        for x in e:

            if x[0] == 1:
                q = p(x[1])
                w = p(x[2])

                if (q == w):
                    ans += 1
                else:
                    pa[q] = w

            if x[0] == 2:
                r = pp(x[1])
                t = pp(x[2])

                if (r == t):
                    ans += 1
                else:
                    pb[r] = t
        tt = 0
        for i in range(1, n + 1):
            if i == pa[i]:
                tt += 1
            if i == pb[i]:
                tt += 1

        if tt != 2:
            return -1
        return ans
