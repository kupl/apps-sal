t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split()))
    c = min(a, b)
    d = max(a, b)
    print(max(2 * c, d) ** 2)
