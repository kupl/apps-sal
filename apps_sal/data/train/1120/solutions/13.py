# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        w = c + d
        x = b - 1 - d + c
        y = a - 1 - c + d
        z = (a - 1 - c) + (b - 1 - d)
        print(max(w, x, y, z))
except:
    pass
