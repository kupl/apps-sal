from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = 30
d = []
# d[i] = 1<<i
for i in range(m+1):
    d.append(1<<i)

c = [[] for i in range(m)]
for bi in b:
    for i in range(m):
        c[i].append(bi&(d[i+1]-1))
for i in range(m):
    c[i].sort()

keta = [0]*m

# しゃくとりするなら桁ごとにやるしか無い
for i in range(m):
    aa = [ai&(d[i+1]-1) for ai in a]
    aa.sort()
    a0 = aa[0]

    i1 = d[i]
    i2 = d[i+1]
    i3 = i2+i1
    b1 = bisect_left(c[i], i1-a0)
    b2 = bisect_left(c[i], i2-a0)
    b3 = bisect_left(c[i], i3-a0)

    for ai in aa:
        # 尺取
        # aiは大きくなる→境界は小さくなる
        # 引いたあとのindexが0以上であることも必要
        while b1-1 >= 0 and c[i][b1-1] >= i1-ai:
            b1 -= 1
        while b2-1 >= 0 and c[i][b2-1] >= i2-ai:
            b2 -= 1
        while b3-1 >= 0 and c[i][b3-1] >= i3-ai:
            b3 -= 1
        keta[i] += b2-b1 + n-b3
    keta[i] %= 2

#print(keta)

ans = 0
for i in range(m):
    ans += keta[i]*(1<<i)

print(ans)
