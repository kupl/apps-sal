t = int(input())
for _ in range(t):
    m, n = map(int, input().strip().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = set(a)
    b = set(b)
    z = b - a
    y = a - b
    print(*y, *z)
