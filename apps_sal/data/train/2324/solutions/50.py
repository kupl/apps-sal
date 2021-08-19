import sys
sys.setrecursionlimit(1000000)

N = int(input())

B = [[]for i in range(N + 1)]

F = [10**10 for i in range(N + 1)]
F[1] = 0
S = [10**10 for i in range(N + 1)]
S[N] = 0

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    B[a].append(b)
    B[b].append(a)

# print(B)


def dfsF(f):
    for i in B[f]:
        if F[i] == 10**10:
            F[i] = F[f] + 1
            dfsF(i)


dfsF(1)


def dfsS(s):
    for i in B[s]:
        if S[i] == 10**10:
            S[i] = S[s] + 1
            dfsS(i)


dfsS(N)
# print(F)
# print(S)
Fennec = 0
Snuke = 0
for i in range(1, N + 1):
    if F[i] <= S[i]:
        Fennec += 1
    else:
        Snuke += 1
if Fennec > Snuke:
    print("Fennec")
else:
    print("Snuke")
