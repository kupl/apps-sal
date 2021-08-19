md = 1000000007
for tst in range(int(input())):
    (n, k) = [int(x) for x in input().split()]
    if n == 0:
        ans = k * (k - 1) % md
        print(ans)
        continue
    z = 0
    if k & 1:
        z = 1
    g = k // 2 + n
    ans = (g + 1) * g
    if z:
        ans = (ans - n) % md
    else:
        ans = (ans - g - g + n) % md
    print(ans)
