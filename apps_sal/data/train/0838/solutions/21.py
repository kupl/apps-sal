for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    m = 0
    b = [i for i in a]
    for i in range(1, n):
        b[i] = b[i - 1] + 1
    for i in range(n):
        m = max(m, a[i] - b[i])
    print(max(b[n - 1] + m, b[n - 1]))
