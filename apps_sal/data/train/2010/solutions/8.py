from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self, n, m):
        m[0] = 1
        for i in range(1, n - 1):
            m[i] = min(m[i - 1] + 1, m[i], i + 1)
        m[n - 1] = 1
        for i in range(n - 2, -1, -1):
            m[i] = min(m[i], m[i + 1] + 1)
        return max(m)


def __starting_point():
    n = int(si.readline().strip())
    m = list(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga(n, m))


'\nhttp://codeforces.com/contest/573/problem/B\n'
__starting_point()
