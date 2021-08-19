n = int(input())
A = list(map(int, input().split()))
a = 0
for i in range(n):
    a = a ^ A[i]
for i in range(n):
    print(a ^ A[i], end=' ')
