from collections import Counter
T = int(input())
for i in range(T):
    NM = []
    A = []
    z = 0
    N = int(input())
    for j in range(N):
        nm, a = input().split()
        NM.append(nm)
        A.append(int(a))
    D = Counter(A)
    K = sorted(D.keys())
    for k in K:
        if D[k] == 1:
            z = k
            break
        else:
            pass
    if z == 0:
        print("Nobody wins.")
    else:
        print(NM[A.index(z)])
