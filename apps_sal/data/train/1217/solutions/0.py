def fun(a, cur, n, cnt):
    if cur >= n - 1:
        return
    for i in range(cur, n - 1):
        if i < n - 2:
            if a[i] > 0 and a[i + 1] > 0:
                a[i] -= 1
                a[i + 1] -= 1
                a[i + 2] += 1
                cnt[0] = (cnt[0] + 1) % 1000000007
                fun(a, i, n, cnt)
                a[i] += 1
                a[i + 1] += 1
                a[i + 2] -= 1
        else:
            if a[i] > 0 and a[i + 1] > 0:
                a[i] -= 1
                a[i + 1] -= 1
                a.append(1)
                cnt[0] = (cnt[0] + 1) % 1000000007
                fun(a, i, n + 1, cnt)
                a[i] += 1
                a[i + 1] += 1
                a.pop()


tc = int(input())
for case in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [1]
    fun(a, 0, n, cnt)
    print(cnt[0] % 1000000007)
