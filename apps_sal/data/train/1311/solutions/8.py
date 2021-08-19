import math
tc = int(input())
for _ in range(tc):
    (n, k) = map(int, input().split())
    ans = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            ans.append(i)
        else:
            ans.append(-i)
    positive = math.ceil(n / 2)
    if positive > k:
        i = n - 1
        needed = positive - k
        while needed > 0:
            if ans[i] > 0:
                ans[i] *= -1
                needed -= 1
            i -= 1
    if positive < k:
        i = n - 1
        needed = k - positive
        while needed > 0:
            if ans[i] < 0:
                ans[i] *= -1
                needed -= 1
            i -= 1
    print(*ans)
