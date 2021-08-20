for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    br = list(map(int, input().split()))
    ma = min(ar)
    mb = min(br)
    ans = 0
    for (i, j) in zip(ar, br):
        r1 = i - ma
        r2 = j - mb
        x = min(r1, r2)
        ans += x
        r1 -= x
        r2 -= x
        ans += r1
        ans += r2
    print(ans)
