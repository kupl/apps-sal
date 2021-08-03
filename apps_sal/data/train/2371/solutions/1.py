def solve():
    n = int(input())
    a = list(map(int, input().split()))
    prev = a[-1]
    cnt = 1
    status = 0
    for i in range(n - 2, -1, -1):
        v = a[i]
        if status == 0:
            if v < prev:
                status = 1
            cnt += 1
            prev = v
            continue
        elif status == 1:
            if v > prev:
                break
            cnt += 1
            prev = v
            continue
    print(n - cnt)


t = int(input())
for _ in range(t):
    solve()
