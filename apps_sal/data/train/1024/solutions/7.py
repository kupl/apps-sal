# python 3.7.1
c, d = 0, 0
for _ in range(int(input())):
    s, n, k, r = input().split()
    s, n, k, r = int(s), int(n), int(k), int(r)
    sum, g, x = 0, k, 0
    a = k
    for i in range(int(n - 1)):
        a = a * r
        g = g + a
    if(g < s):
        x = s - g
        print("POSSIBLE", x)
        c = c + x
    else:
        x = g - s
        print("IMPOSSIBLE", x)
        d = d + x
if c > d:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
