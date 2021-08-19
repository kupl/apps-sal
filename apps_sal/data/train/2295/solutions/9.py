N = int(input())
a = [0] * N
b = [0] * N
for i in range(N):
    (a1, b1) = map(int, input().split())
    a[i] = a1
    b[i] = b1
total = sum(a)
minans = total
for i in range(N):
    if a[i] > b[i]:
        minans = min(minans, b[i])
if minans == total:
    print(0)
else:
    print(total - minans)
