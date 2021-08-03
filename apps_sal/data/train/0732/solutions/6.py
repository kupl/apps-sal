T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]

    xa = 0
    xb = 0
    distance = 0

    for i in range(N):
        if(xa == xb and A[i] == B[i]):
            distance += A[i]
        xa += A[i]
        xb += B[i]

    ans.append(distance)

for i in ans:
    print(i)
