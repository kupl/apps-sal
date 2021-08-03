# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = 1000000007
        d = n**3
        f = (n - 1)**2
        g = (d + f) % M
        print(g)
except:
    pass
