t = int(input())
for x in range(t):
    d = []
    (n, m_len) = list(map(int, input().split()))
    m = [int(x) for x in input().split()]
    m.sort()
    (a, b) = (m[0], m[-1])
    for y in range(n):
        d.append(max(y - a, b - y))
    print(*d)
