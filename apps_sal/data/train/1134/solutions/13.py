from math import ceil
for _ in range(eval(input())):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    sum = 0
    for i in range(M):
        sum += A[i]
    for i in range(M, N):
        sum -= ceil(A[i] / 2)
    if(sum < 0):
        print("DEFEAT")
    else:
        print("VICTORY")
