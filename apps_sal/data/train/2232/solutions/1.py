
N = int(input())

x = 2

for i in range(1, N + 1):
    u, v = i, i + 1
    p = u**2 * v**2
    d = p - x
    z = d // u
    assert(z <= 10**18)
    print(z)
    x = u * v
