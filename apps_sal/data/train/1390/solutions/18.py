t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    ans = a + b - a / (b + 1)
    ans = round(ans, 6)
    print(ans)
