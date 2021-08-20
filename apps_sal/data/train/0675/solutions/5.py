def func(n):
    k = n
    if k == 1:
        return [1]
    while k % 2 == 0:
        k = k // 2
    if k == 1:
        return -1
    ans = [i for i in range(1, n + 1)]
    i = 2
    while i < n:
        (ans[i - 1], ans[i]) = (ans[i], ans[i - 1])
        i *= 2
    if n < 4:
        return ans
    return [2, 3, 1, 5, 4] + ans[5:]


for _ in range(int(input())):
    n = int(input())
    ans = func(n)
    if type(ans) == int:
        print(-1)
    else:
        print(*ans)
