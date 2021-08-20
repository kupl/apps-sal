n = int(input())
arr = [int(t) for t in input().split()]
arr.sort()
nx = 0
i = 0
res = 0
while i < n:
    j = i
    while j < n and arr[i] == arr[j]:
        j += 1
    nx = max(nx, j)
    t = min(j - i, n - nx)
    nx += t
    nx = min(nx, n)
    res += t
    i = j
print(res)
