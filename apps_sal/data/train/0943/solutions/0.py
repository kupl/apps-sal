# cook your dish here
t = int(input())
for i in range(t):
    v, w = list(map(int, input().strip().split(" ")))
    if v == w:
        print(v + 1)
    elif v < w:
        print(v + 1)
    else:
        print(w + 1)
        # s="a"
        # s=s*v
        # l=list(s)
        # print(l)
        ct = 0
        # for i in range(w):
