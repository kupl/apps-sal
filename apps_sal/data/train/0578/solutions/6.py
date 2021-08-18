def closestNumber(n, m):
    q = int(n / m)

    n1 = m * q

    if((n * m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    if (abs(n - n1) < abs(n - n2)):
        return n1

    return n2


T = int(input())
for j in range(1, T + 1):
    N, B = input().split()
    N = int(N)
    B = int(B)
    p = N % B
    k = N
    fs = 0
    maxim = 0

    print(int((N - closestNumber(int(N / 2), B)) * (closestNumber(int(N / 2), B)) / B))
