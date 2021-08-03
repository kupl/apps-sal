t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    if n == 0:
        ans = (k - 1) * k
        print(ans % 1000000007)
        continue
    k -= 1
    if k == 0:
        ans = n * (n - 1) + n
        print(ans % 1000000007)
    elif k % 2 != 0:
        p = n + (k // 2)
        ans = p * (p + 1) + n
        print(ans % 1000000007)
    else:
        k -= 2
        p = n + (k // 2)
        ans = p * (p + 1) + (p + 1) + (p + 1 - n)
        print(ans % 1000000007)
