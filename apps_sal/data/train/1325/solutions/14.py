t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    print(d - b, d - c, d - a)
