(k, q) = list(map(int, input().split()))
t = [0] * (k + 1)
t[1] = 1
d = [0]
n = i = 1
while i < 1001:
    if 2000 * t[k] > i - 1e-07:
        d.append(n)
        i += 1
    else:
        t = [0] + [(j * t[j] + (k - j + 1) * t[j - 1]) / k for j in range(1, k + 1)]
        n += 1
for i in range(q):
    print(d[int(input())])
