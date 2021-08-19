import sys
n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
m = 0
for i in range(1, n):
    if len(b) > 0:
        m = max(m, b[-1] ^ a[i])
    while len(b) > 0 and a[i] > b[-1]:
        m = max(m, b[-1] ^ a[i])
        b.pop()
    if len(b) > 0:
        m = max(m, b[-1] ^ a[i])
    b.append(a[i])
print(m)
