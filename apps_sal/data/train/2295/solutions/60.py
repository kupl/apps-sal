N = int(input())
A = []
B = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

if A == B:
    print((0))
else:
    M = sum(A)
    c = 10**10
    for a, b in zip(A, B):
        if a > b:
            c = min(c, b)
    print((M - c))
