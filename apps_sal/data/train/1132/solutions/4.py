a = list(map(int, open(0)))[1:]
N = max(a) + 1
b = [1] * N
for i in range(1, N):
    j = 2 * i
    b[i] = b[i - 1] * j * (j - 1) // 2 % (10**9 + 7)

for n in a:
    print(b[n])
