n = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))


def tree_cutting(n, A, B):
    C = [0 for _ in range(n)]
    hullx = [0 for _ in range(n)]
    hully = [0 for _ in range(n)]

    sz = 0
    p = 0

    C[0] = 0
    hullx[0] = B[0]
    hully[0] = C[0]

    for i in range(1, n):
        p = min(sz, p)
        while sz > 0 and p < sz and (hully[p + 1] - hully[p]) / (hullx[p] - hullx[p + 1]) <= A[i]:
            p += 1
        C[i] = hully[p] + hullx[p] * A[i]
        sz += 1
        hullx[sz] = B[i]
        hully[sz] = C[i]
        while sz > 1 and (hully[sz - 2] - hully[sz - 1]) / (hullx[sz - 1] - hullx[sz - 2]) >= (hully[sz - 2] - hully[sz]) / (hullx[sz] - hullx[sz - 2]):
            hullx[sz - 1] = hullx[sz]
            hully[sz - 1] = hully[sz]
            sz -= 1
    return C[n - 1]


print(tree_cutting(n, A, B))
