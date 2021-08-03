# cook your dish here
t = int(input())
for i in range(0, t):
    s = int(input())
    g = []
    for i in range(0, s):
        k = int(input())
        g.append(k)
    print(max(g))
