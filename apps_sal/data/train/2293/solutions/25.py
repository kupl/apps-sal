N = int(input())
A = [(int(a), 0) for a in input().split()]
def combine(a, b): return a if a[1] >= b[0] else b if b[1] >= a[0] else (a[0], b[0]) if a[0] > b[0] else (b[0], a[0])


for i in range(N):
    ii = 1 << i
    for j in range(1 << N)[::-1]:
        if j & ii:
            A[j] = combine(A[j], A[j ^ ii])

ANS = [0] * (1 << N)
for i in range(1, 1 << N):
    ANS[i] = max(ANS[i - 1], sum(A[i]))

print("\n".join(map(str, ANS[1:])))
