N = 100001
a = [1] * N
for i in range(1, N):
 j = 2 * i
 a[i] = a[i - 1] * j * (j - 1) // 2 % (10**9 + 7)

for s in[*open(0)][1:]:
 print(a[int(s)])

