from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        l = list(map(int, input().split()))
        mex = 0
        d = defaultdict(lambda: [])
        for (i, num) in enumerate(l):
            d[num - 1].append(i + 1)

        def dfs(i):
            mex = 0
            size = 1
            for j in d[i]:
                if i == j:
                    continue
                x = dfs(j)
                mex = max(mex, x[0])
                size += x[1]
            return [mex + size, size]
        print(dfs(0)[0])
