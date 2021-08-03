N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = []

seen = {}
flag = False

for i in range(N):
    for j in range(M):
        if(len(ans) == N + M - 1):
            flag = True
            break
        if(A[i] + B[j] not in seen):
            ans.append('{} {}'.format(i, j))
            seen[A[i] + B[j]] = True
    if(flag):
        break

for i in ans:
    print(i)
