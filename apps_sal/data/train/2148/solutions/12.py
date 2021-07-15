from sys import stdin

_, *l = stdin.read().splitlines()
for i, s in enumerate(l):
    p, q, b = map(int, s.split())
    l[i] = 'Infinite' if p * pow(b, 64, q) % q else 'Finite'
print('\n'.join(l))
