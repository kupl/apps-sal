t = int(input())
for _ in range(t):
    (s, n) = [int(x) for x in input().split()]
    ans = 0
    if s == n:
        ans = 1
    elif s > n:
        ans += s // n
        s = s % n
        if s % 2 == 1:
            ans += 1
        if s != 1 and s != 0:
            ans += 1
    else:
        if s % 2 == 1:
            ans += 1
        if s != 1 and s != 0:
            ans += 1
    print(ans)
