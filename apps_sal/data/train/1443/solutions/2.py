# cook your dish here
w = int(input())
for i in range(w):
    B, f = list(map(int, input().split()))
    v = []
    for j in range(B):
        j = list(input())
        v.append(j)
    q = 0
    for k in range(f):
        s = 0
        for n in range(B):
            if v[n][k] == '1':
                s += 1
        if s > 1:
            q += ((s * (s - 1)) // 2)
    print(q)
