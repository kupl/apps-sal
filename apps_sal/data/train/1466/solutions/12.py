
n, q = [int(a) for a in input().strip().split()]

F = [int(a) for a in input().strip().split()]

S = [0]

for i in range(n):
    S.append(S[i] ^ F[i])

for _ in range(q):
    k = int(input())
    print(S[k % (n + 1)])
