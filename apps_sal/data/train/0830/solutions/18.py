T = int(input())
for _ in range(T):
    N = int(input())
    A = input()
    B = input()
    dupdel = list(dict.fromkeys(B))

    def notpossible(A, B, dupdel):
        for i in range(len(dupdel)):
            if dupdel[i] not in A:
                return -1
        for i in range(len(A)):
            if A[i] < B[i]:
                return -1
    if notpossible(A, B, dupdel) == -1:
        print(-1)
        continue
    else:
        L = []
        for i in range(len(A)):
            if A[i] != B[i]:
                L.append(B[i])
        P = list(dict.fromkeys(L))
        print(len(P))
        P.sort(reverse=True)
        for i in range(len(P)):
            Q = []
            R = []
            for j in range(len(A)):
                if B[j] == P[i]:
                    Q.append(j)
                    R.append(A[j])
            if P[i] not in R:
                for k in range(N):
                    if A[k] == P[i]:
                        Q.append(k)
                        break
            print(len(Q), *Q)
