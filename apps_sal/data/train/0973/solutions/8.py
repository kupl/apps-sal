t = int(input())
while t > 0:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()[:n]))
    m1 = max(a)
    m2 = min(a)
    m1 = m1 + k
    m2 = m2 - k
    print(m1 - m2)
