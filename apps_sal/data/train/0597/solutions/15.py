# cook your dish here

T = int(input())
t = 0
while t < T:
    t += 1
    N = int(input())
    h, x = list(), list()
    for i in range(N):
        a, b = list(map(int, input().split()))
        h.append(b)
        x.append(a)

    v = []
    for i in range(N):
        v.append(x[min(i + 1, N - 1)] - x[max(i - 1, 0)])
    h.sort()
    v.sort()

    ans = 0
    for i in range(N):
        ans += h[i] * v[i]

    print(ans)
