n = int(input())
A = list(map(int, input().split()))
k = int(input())
i = 0
res = 0
tmp = 0
while i <= k:
    tmp = sum(A[:i]) + sum(A[(n - k + i):])
    if tmp > res:
        res = tmp
    i += 1
print(res)
