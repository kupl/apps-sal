def mod(f, m):
    if f == 1:
        return 2 % m
    elif f % 2 == 0:
        return mod(f // 2, m) ** 2 % m
    else:
        return mod(f // 2, m) ** 2 * 2 % m


(n, m) = list(map(int, input().strip().split()))
l = [0 for i in range(n + 1)]
(l[0], l[1]) = (1, 1)
for i in range(2, n + 1):
    if l[i] == 0:
        t = 2
        while t * i <= n:
            l[t * i] = 1
            t += 1
prime = []
for i in range(len(l)):
    if l[i] == 0:
        prime.append(i)
t = 0
for j in prime:
    if n % j == 0:
        t += mod(n // j, m)
s = mod(n, m)
t %= m
if s - t > 0:
    print(s - t)
else:
    print(m - s + t)
