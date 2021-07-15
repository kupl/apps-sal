nKnights, nFights = map(int,input().split())
anext = [i + 1 for i in range(nKnights + 1)]
result = [0] * nKnights
for _ in range(nFights):
    l, r, x = map(int,input().split())
    i = l
    while i <= r:
        if result[i-1]==0 and i!=x:
            result[i-1] = x
        temp = anext[i]
        if i < x:
            anext[i] = x
        else:
            anext[i] = r + 1
        i = temp
print(*result)
