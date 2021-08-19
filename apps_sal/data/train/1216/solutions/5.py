T = int(input())
for i in range(T):
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))[:N]
    for j in range(len(A)):
        if A[j] >= K:
            print('YES')
            break
    else:
        print('NO')
