t = int(input())
for i in range(t):
    (a, b, c) = map(int, input().split())
    k = (c - b) // a
    print(k * a + b)
