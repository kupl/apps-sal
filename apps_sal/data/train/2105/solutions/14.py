n = int(input()) + 2

prime = [i % 2 for i in range(n)]
prime[1] = 0
prime[2] = 1
for p in range(3, int(n**0.5) + 2, 2):
    if not prime[p]:
        continue
    for q in range(p * p, n, p + p):
        prime[q] = 0

l = [2 - x for x in prime[2:]]
print(max(l))
print(" ".join(map(str, l)))
