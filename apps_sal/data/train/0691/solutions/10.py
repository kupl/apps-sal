t = int(input())
for z in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    h = [0] * 1000001
    m = 0
    for j in range(n - 1, 1, -1):
        x = j - 1
        c = 0
        if h[a[j]] == 0:
            while x >= 0:
                if a[x] % a[j] == 0:
                    h[a[x]] = 1
                    c = c + 1
                x = x - 1
            m = max(m, c)
            h[a[j]] = 1
    print(m)
