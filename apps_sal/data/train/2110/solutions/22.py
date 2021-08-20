n = int(input())
A = list(map(int, input().split()))
d = {}
for i in range(n):
    if A[i] in d:
        k = A[i]
        while k in d:
            del d[k]
            k += 1
        d[k] = 1
    else:
        d[A[i]] = 1
print(len(d))
