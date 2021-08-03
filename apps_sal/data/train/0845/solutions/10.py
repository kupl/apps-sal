t = int(input())

for i in range(t):
    m, n = map(int, input().split())

    mul = m * n

    while(m != n):
        if (m > n):
            m -= n
        else:
            n -= m
    print(mul // (m * n))
