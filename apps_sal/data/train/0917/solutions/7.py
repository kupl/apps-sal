t = int(input())
while t > 0:
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    x = 3 * 10 ** 9
    a = []
    for i in range(n):
        for j in range(i + 1, n):
            a.append(abs(l[j] + l[i] - k))
    m = min(a)
    print(m, a.count(m))
    t -= 1
