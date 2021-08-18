t = int(input())
for i in range(t):

    n = int(input())
    s = input()
    l = s.count("L")
    r = s.count("R")
    u = s.count("U")
    d = s.count("D")
    k = abs(l - r)
    p = abs(u - d)
    print(n - (k + p))
