for i in range(int(input())):
    n, m, k = [int(i) for i in input().split()]
    ans = 0
    l = [int(i) for i in input().split()]
    for i in l:
        r = i // m + 1
        c = i % m
        if(c == 0):
            c = m
            r -= 1
        ans += r * (n + 1 - r) * c * (m + 1 - c)
    ans /= ((n + 1) * (m + 1) * n * m) // 4
    print(ans)
