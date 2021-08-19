n = int(input())
queries = list((input().split() for _ in range(n)))
(a, b) = (0, (1 << 10) - 1)
for (c, x) in queries:
    x = int(x)
    if c == '|':
        (a, b) = (a | x, b | x)
    elif c == '&':
        (a, b) = (a & x, b & x)
    elif c == '^':
        (a, b) = (a ^ x, b ^ x)
(x, y, z) = (0, (1 << 10) - 1, 0)
for i in range(10):
    a_i = a >> i & 1
    b_i = b >> i & 1
    if a_i and b_i:
        x |= 1 << i
    if not a_i and (not b_i):
        y ^= 1 << i
    if a_i and (not b_i):
        z ^= 1 << i
print(3)
print('|', x)
print('&', y)
print('^', z)
