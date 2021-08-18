for _ in range(int(input())):
    n, p = map(int, input().split())
    l = [int(i) for i in input().split()]
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + l[i - 1]
        pre[i] %= p
    cmaxi = 0
    maxi = 0
    for i in range(n):
        for j in range(i, n):
            curr = (pre[j + 1] - pre[i] + p) % p
            if curr > maxi:
                maxi = curr
                cmaxi = 1
            elif curr == maxi:
                cmaxi += 1
    print(maxi, cmaxi)
