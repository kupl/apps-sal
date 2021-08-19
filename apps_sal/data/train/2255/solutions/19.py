n = int(input())
a = list(map(int, input().split()))
a = [0] + a
x = [0] * (n + 1)
c = {0: 1}
sol = 0
for i in range(1, n + 1):
    x[i] = x[i - 1] ^ a[i]
    if x[i] * 2 + i % 2 in c:
        sol += c[x[i] * 2 + i % 2]
    try:
        c[x[i] * 2 + i % 2] += 1
    except KeyError:
        c[x[i] * 2 + i % 2] = 1
print(sol)
