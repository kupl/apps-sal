(n, m) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
s = sum(a)
if s < n:
    print(-1)
else:
    r = []
    diff = s - n
    curr = 0
    valid = True
    for i in range(m):
        r.append(curr + 1)
        curr += a[i]
        if curr > n:
            valid = False
        d = min(diff, a[i] - 1)
        curr -= d
        diff -= d
    if valid:
        print(*r)
    else:
        print(-1)
