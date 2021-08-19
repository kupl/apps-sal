# cook your dish here
t = int(input())

for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    e = (a + c) - d
    f = (a + b) - d
    g = (b + c) - d
    print(e, f, g)
