t = eval(input())
for _ in range(t):
    (n, d) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = sum(a)
    if s % n != 0:
        print(-1)
        continue
    each = s / n
    (ans, ok) = (0, True)
    for i in range(d):
        (cur, rem) = (i, 0)
        while cur < n:
            rem = a[cur] + rem - each
            ans += abs(rem)
            cur += d
        if rem != 0:
            ok = False
            break
    print(ans if ok else -1)
