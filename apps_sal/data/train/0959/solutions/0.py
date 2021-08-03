for i in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))[:n]
    m.sort()
    t = 0
    for j in range(n // 2):
        t += abs(m[j] - m[n - j - 1])
    print(t)
