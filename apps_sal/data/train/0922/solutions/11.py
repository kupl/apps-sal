t = int(input())
for _ in range(t):
    (m, n) = map(int, input().strip().split())
    x = list(map(int, input().split()))
    f = list(map(int, input().split()))
    print(*(set(x) | set(f)) - (set(x) & set(f)))
