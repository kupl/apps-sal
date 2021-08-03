import math
N = int(input())
X = list(map(int, input().split()))

L = int(input())
M = N.bit_length() + 3
doub = [[0 for _ in range(N)] for _ in range(M)]

r = 0
for l in range(N):
    db = doub[0]
    while r < N and X[r] <= X[l] + L:
        r += 1
    r -= 1
    db[l] = r

for i in range(1, M):
    db = doub[i]
    dbp = doub[i - 1]
    for l in range(N):
        db[l] = dbp[dbp[l]]
#print(*doub, sep="\n")


def db_query(a, b):  # aからbへ行く時の回数
    ans = 0
    tmp = a
    d = N.bit_length()
    while d >= 0:
        #print(a,b, d,ans,tmp,doub[d][tmp])
        if doub[d][tmp] < b:
            ans += pow(2, d)
            tmp = doub[d][tmp]
        d -= 1
    return ans + 1


Q = int(input())
for _ in range(Q):
    a, b = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    print((db_query(a, b)))
