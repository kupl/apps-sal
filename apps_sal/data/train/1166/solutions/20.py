N = int(input())
A = [int(x) for x in input().split()]
for _ in range(int(input())):
    K = int(input())
    total = 0
    for i in range(N):
        a = 0
        count = 0
        forward = 0
        backward = 1
        if A[i] == K:
            if i != A.index(K):
                a = 1
            for j in range(i, N):
                if A[j] >= K:
                    forward += 1
                else:
                    break
            for j in range(i - 1, -1, -1):
                if a == 1:
                    if A[j] > K:
                        backward += 1
                    else:
                        break
                elif a == 0:
                    if A[j] >= K:
                        backward += 1
                    else:
                        break
            count += forward * backward
            total += count
    print(total)
