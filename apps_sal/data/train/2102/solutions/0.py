k = int(input())
p = [['0'] * 100 for j in range(100)]
def g(n): return n * (n * n - 1) // 6


i = n = 0
while g(n + 1) <= k:
    n += 1
while i < n + 1:
    for j in range(i):
        p[i][j] = p[j][i] = '1'
    i += 1
k -= g(n)
def g(n): return n * n - n >> 1


while k:
    n = 0
    while g(n + 1) <= k:
        n += 1
    for j in range(n):
        p[i][j] = p[j][i] = '1'
    k -= g(n)
    i += 1
print(i)
for j in range(i):
    print(''.join(p[j][:i]))
