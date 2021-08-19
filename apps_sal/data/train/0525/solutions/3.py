t = int(input())
for _ in range(t):
    (a, b, c) = list(map(int, input().split()))
    print((c - b) // a * a + b)
