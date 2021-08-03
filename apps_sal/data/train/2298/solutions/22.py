N, T = list(map(int, input().split()))
A = list(map(int, input().split()))
mxx, mnx = 0, 10**18
for a in A:
    if a - mnx > mxx:
        c, mxx = 1, a - mnx
    elif a - mnx == mxx:
        c += 1
    mnx = min(mnx, a)
print(c)
