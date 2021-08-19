# cook your dish here

t = int(input())
for _ in range(t):
    p, idx = list(map(int, input().split()))
    n = 2**p - 1
    l = []
    s = 0
    while(p > 0):
        l.append(int(idx % 2))
        idx = idx / 2
        p -= 1
    for i in l:
        s = s * 2 + i
    print(s)
