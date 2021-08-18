n = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
C = [0 for _ in range(n)]
hullx = [0 for _ in range(n)]
hully = [0 for _ in range(n)]

sz = -1
p = 0


def intersection(p, q):
    nonlocal hullx, hully
    return (hully[q] - hully[p]) / (hullx[p] - hullx[q])


def insert(B, C):
    nonlocal sz, p, hullx, hully
    sz += 1
    hullx[sz] = B
    hully[sz] = C
    while sz > 1 and intersection(sz - 1, sz - 2) >= intersection(sz - 1, sz):
        hullx[sz - 1] = hullx[sz]
        hully[sz - 1] = hully[sz]
        sz -= 1


def query(x):
    nonlocal sz, p, B, C
    p = min(sz, p)
    while sz > 0 and p < sz and intersection(p, p + 1) <= x:
        p += 1
    return hully[p] + hullx[p] * x


C[0] = 0
insert(B[0], 0)

for i in range(1, n):
    C[i] = query(A[i])
    insert(B[i], C[i])
print(C[n - 1])
