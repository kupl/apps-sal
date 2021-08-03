T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))[:N]
    B = set(A)
    L = []
    for j in range(len(B)):
        L.append(A.count(A[j]))
    print(len(A) - max(L))
