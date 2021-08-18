
t = int(input())
for _ in range(t):
    p, id1 = list(map(int, input().split()))
    n = pow(2, p) - 1
    l = []
    res = 0
    while(p > 0):
        l.append(int(id1 % 2))
        id1 = id1 / 2
        p -= 1
    for i in l:
        res = res * 2 + i
    print(res)
