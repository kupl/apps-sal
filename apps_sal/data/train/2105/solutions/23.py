n = int(input())
prime = [True] * (n + 2)
prime[0] = prime[1] = False
for m in range(2, n + 2):
    if prime[m]:
        for i in range(2 * m, n + 2, m):
            prime[i] = False
print('2' if n > 2 else '1')
colors = ['1' if prime[m] else '2' for m in range(2, n + 2)]
print(' '.join(colors))
