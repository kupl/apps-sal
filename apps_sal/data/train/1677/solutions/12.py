from itertools import accumulate
import copy
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = copy.deepcopy(B)
for i in range(1, len(C)):
    C[i] += C[i - 1]
answer = 0
temp = 0
for i in range(N):
    for j in range(N):
        temp = 0
        if i == j:
            temp = A[i]
        elif i < j:
            temp += A[i] + A[j] + C[j - 1] - C[i]
        else:
            temp += A[i] + A[j] + C[N - 1] - C[i] + C[j] - B[j]
        if temp > answer:
            answer = temp + 0
print(answer)
