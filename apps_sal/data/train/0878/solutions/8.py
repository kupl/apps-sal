# cook your dish here
for _ in range(int(input())):
    M, L = map(int, input().split())
    g = list(map(int, input().split()))
    g.insert(0, 0)
    b = 0
    for i in range(1, M + 1):
        b += (g[i] - g[i - 1] - 1) // L
    print(b)
