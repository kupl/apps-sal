S = input()
T = input()
N = len(S)
M = len(T)
U = [0 for i in range(N + 1)]
V = [0 for i in range(M + 1)]
for i in range(N):
    if S[i] == "A":
        U[i + 1] = (U[i] + 1) % 3
    else:
        U[i + 1] = (U[i] - 1) % 3
for i in range(M):
    if T[i] == "A":
        V[i + 1] = (V[i] + 1) % 3
    else:
        V[i + 1] = (V[i] - 1) % 3
q = int(input())
O = ["" for i in range(q)]
for inp in range(q):
    a, b, c, d = list(map(int, input().split()))
    if (U[b] - U[a - 1] - V[d] + V[c - 1]) % 3 == 0:
        O[inp] = "YES"
    else:
        O[inp] = "NO"
for i in O:
    print(i)
