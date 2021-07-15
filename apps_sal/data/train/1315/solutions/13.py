n = int(input())
A = {}
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    for i in range(3):
        a[i] = str(a[i])
    s = ''.join(a)
    if s in A:
        A[s] += 1
    else:
        A[s] = 1

count = 0
for i in A:
    if A[i] == 1:
        count += 1
print(count)
