(N, T) = map(int, input().split())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
Bl = [set() for i in range(N)]
B[N - 1] = A[N - 1]
Bl[N - 1].add(N - 1)
for i in range(N - 2, -1, -1):
    if A[i] > B[i + 1]:
        B[i] = A[i]
        Bl[i].add(i)
    elif A[i] == B[i + 1]:
        B[i] = B[i + 1]
        Bl[i] = Bl[i + 1] + {i}
    elif A[i] < B[i + 1]:
        B[i] = B[i + 1]
        Bl[i] = Bl[i + 1]
C = [B[i] - A[i] for i in range(N)]
'\nprint(A)\nprint(B)\nprint(Bl)\nprint(C)\n'
Cm = max(C)
Cml = set()
for i in range(N):
    if C[i] == Cm:
        Cml.update(Bl[i])
'\nprint(Cm)\nprint(Cml)\n'
ans = len(Cml)
print(ans)
