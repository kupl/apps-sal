# cook your dish here
import math

try:
    tc = int(input())
    for _ in range(tc):
        n, k = list(map(int, input().split()))
        ans = []
        need = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                ans.append(i)
            else:
                ans.append(-i)
        p = math.ceil(n / 2)

        need = p - k if p > k else k - p

        if k < p:
            i = n - 1
            while need > 0:
                if ans[i] > 0:
                    ans[i] *= -1
                    need -= 1
                i -= 1

        if k > p:
            i = n - 1
            while need > 0:
                if ans[i] < 0:
                    ans[i] *= -1
                    need -= 1
                i -= 1
        print(*ans)
except:
    pass
