t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    x = (c - b) // a
    print((x * a) + b)
