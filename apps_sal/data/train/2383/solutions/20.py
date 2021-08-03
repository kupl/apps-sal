t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    s = min(max(a * 2, b), max(a, b * 2))
    print(s * s)
