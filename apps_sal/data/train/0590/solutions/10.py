T = int(input())
for i in range(T):
    (n, x, m) = list(map(int, input().split()))
    l1 = [int(i) for i in input().split()]
    if x == 1:
        l1[0] = l1[0] % 1000000007
        print(l1[0])
    elif x == 2:
        m = m % 1000000007
        l1[0] = l1[0] % 1000000007
        l1[1] = (l1[1] % 1000000007 + l1[0] * m % 1000000007) % 1000000007
        print(l1[1])
    else:
        m = m % 1000000007
        c = -1
        y = 0
        q = 1
        y = l1[x - 1] % 1000000007
        for j in range(x - 2, -1, -1):
            c = c + 1
            q = q * ((m + c) % 1000000007) % 1000000007
            s = q * pow(c, 1000000005, 1000000007) % 1000000007
            y = (y + s * (l1[j] % 1000000007) % 1000000007) % 1000000007
        print(y)
